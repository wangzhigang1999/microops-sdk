import json
import os
import pickle
from abc import abstractmethod

import pandas as pd
from loguru import logger

from sdk.config.inference_config import InferenceConfig
from sdk.config.kafka_config import KafkaConfig
from sdk.config.mongo_config import MongoConfig
from sdk.config.redis_config import RedisConfig
from sdk.config.train_config import TrainConfig


class AlgoTemplate:
    def __init__(self):

        self.model = None

        try:
            self.mode = os.environ["MODE"]
        except KeyError:
            self.mode = "train"

        if self.mode == "train":
            self.train_config: TrainConfig = self.load_train_config()
        elif self.mode == "inference":
            self.inference_config: InferenceConfig = self.load_inference_config()

        self.build_model()

    def build_model(self):
        self.model = self.load_model()

    @staticmethod
    def parse_config(config) -> (str, object):
        if config["type"] == "KAFKA":
            kafkaConfig = KafkaConfig(config["host"], config["port"], config["properties"], config["username"], config["password"])
            return "kafkaConfig", kafkaConfig

        elif config["type"] == "REDIS":
            redisConfig = RedisConfig(config["host"], config["port"], config["password"], config["properties"])
            return "redisConfig", redisConfig

        elif config["type"] == "MONGO":
            mongoConfig = MongoConfig(config["host"], config["port"], config["username"], config["password"], config["properties"])
            return "mongoConfig", mongoConfig

        elif config["type"] == "JOB":
            model_name = config["name"]
            return "model_name", model_name

    @staticmethod
    def load_inference_config() -> InferenceConfig:
        configs: list = json.loads(os.environ["SCHEDULE_CONFIG"])
        cfg = InferenceConfig()
        for config in configs:
            attr, config = AlgoTemplate.parse_config(config)
            cfg.__setattr__(attr, config)
        return cfg

    @staticmethod
    def load_train_config() -> TrainConfig:
        configs: list = json.loads(os.environ["TRAIN_CONFIG"])
        cfg = TrainConfig()
        for config in configs:
            attr, config = AlgoTemplate.parse_config(config)
            cfg.__setattr__(attr, config)
        return cfg

    def train(self):

        logger.info("..............Starting training..............")

        logger.info("..............Loading data..............")
        # load data
        data = self.train_config.getMongoClient().get_all(self.train_config.mongo.db,
                                                          self.train_config.mongo.collection,
                                                          query={"timestamp": {"$gte": self.train_config.mongo.start_time,
                                                                               "$lte": self.train_config.mongo.end_time}})

        #  convert to pandas dataframe
        frame = pd.DataFrame(data)
        logger.info("Raw Data shape: {}".format(frame.shape))

        frame = self.preprocess(frame)
        logger.info("Preprocessed Data shape: {}".format(frame.shape))

        # train model
        model = self.train_model(frame)
        self.save_model(model)

    @abstractmethod
    def predict(self, x):
        pass

    def save_model(self, model):
        if model is not None:
            model_b = pickle.dumps(model, protocol=None, fix_imports=True)
            self.train_config.getRedisClient().set(self.train_config.model_name, model_b)
            logger.info("Model saved to redis")
        else:
            logger.error("Model is None, not saving")

    def load_model(self):
        logger.info("Loading model from redis")
        try:
            model_b = self.inference_config.getRedisClient().get(self.inference_config.model_name)
            model = pickle.loads(model_b)
            logger.info("Model loaded from redis")
        except Exception as e:
            logger.error("Error loading model from redis: {}".format(e))
            model = None
        return model

    def start(self):
        mode = str(self.mode).lower()
        if mode == "train":
            self.train()
        elif mode == "inference":
            self.inference()

    @abstractmethod
    def train_model(self, frame) -> object:
        pass

    def preprocess(self, frame):
        # sort by timestamp
        frame = frame.sort_values(by="timestamp")

        # drop _id
        frame.drop("_id", axis=1, inplace=True)

        # fill missing values
        frame.fillna(method="ffill", inplace=True)

        # drop timestamp
        frame.drop("timestamp", axis=1, inplace=True)

        # drop constant columns
        frame = frame.loc[:, frame.apply(pd.Series.nunique) != 1]
        return frame

    @abstractmethod
    def inference(self):
        pass


if __name__ == '__main__':
    algo = AlgoTemplate()
    algo.start()
