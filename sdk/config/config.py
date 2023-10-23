import json
import os

from sdk.config.datasource.kafka_datasource import KafkaDataSource
from sdk.config.datasource.mongo_datasource import MongoDataSource
from sdk.config.storage.mongo_storage import MongoStorage
from sdk.config.storage.redis_storage import RedisStorage
from sdk.config.storage.result_storage import ResultStorage
from sdk.config.storage.model_storage import ModelStorage
from sdk.config.algorithm import Algorithm
from loguru import logger


class Config(object):
    MONGO_CONST = "MONGODB"
    REDIS_CONST = "REDIS"
    KAFKA_CONST = "KAFKA"

    def __init__(self):
        self.__mode = os.environ.get('MODE', 'TRAIN')
        # logger.info("current mode is {}".format(self.mode))
        self.json_config = json.loads(os.environ.get('CONFIG', '{}'))

        self.__model_path = self.json_config["modelPath"]
        self.__result_path = self.json_config["resultPath"]

        self.__init_storage()
        self.__init_datasource()

        self.__algorithm = Algorithm(self.json_config["algorithm"])
        self.__dataset_start_time = self.json_config["datasetStartTime"]
        self.__dataset_end_time = self.json_config["datasetEndTime"]
        self.__selected_fields = self.json_config["selectedFields"]

        self.__hyper_params = self.json_config["hyperParams"]

        self.__target = self.json_config["target"] if self.mode != "TRAIN" else None

        # for each key, try to convert to int, if not possible, keep it as string
        for key in self.__hyper_params:
            try:
                self.__hyper_params[key] = int(self.__hyper_params[key])
            except ValueError:
                pass

    def __init_storage(self):
        storage_list = self.json_config["storage"]
        for storage in storage_list:
            if storage["usage"] == "model":
                self.__model_storage = ModelStorage(Config.__get_storage_instance(storage))
            elif storage["usage"] == "result":
                self.__result_storage = ResultStorage(Config.__get_storage_instance(storage))
            else:
                logger.error("unknown storage usage: {}".format(storage["usage"]))
                return

    @staticmethod
    def __get_storage_instance(storage):
        storage_type = storage["type"]
        if storage_type == Config.REDIS_CONST:
            return RedisStorage(storage)
        elif storage_type == Config.MONGO_CONST:
            return MongoStorage(storage)
        else:
            logger.error("unknown storage type: {}".format(storage["type"]))
            return

    def __init_datasource(self):
        datasource = self.json_config["dataSource"]
        if self.mode == "TRAIN":
            self.__train_datasource = Config.__get_datasource_instance(datasource)
        elif self.mode == "INFERENCE":
            # inference only need a stream handler
            self.__inference_datasource = Config.__get_datasource_instance(datasource)

    @staticmethod
    def __get_datasource_instance(datasource):
        datasource_type = datasource["type"]
        if datasource_type == Config.MONGO_CONST:
            return MongoDataSource(datasource)
        elif datasource_type == Config.KAFKA_CONST:
            return KafkaDataSource(datasource)
        else:
            logger.error("unknown datasource type: {}".format(datasource["type"]))
            return

    @property
    def mode(self):
        return self.__mode

    @property
    def model_path(self):
        return self.__model_path

    @property
    def result_path(self):
        return self.__result_path

    @property
    def algorithm(self):
        return self.__algorithm

    @property
    def model_storage(self):
        return self.__model_storage

    @property
    def result_storage(self):
        return self.__result_storage

    @property
    def train_datasource(self):
        return self.__train_datasource

    @property
    def inference_datasource(self):
        return self.__inference_datasource

    @property
    def dataset_start_time(self):
        return self.__dataset_start_time

    @property
    def dataset_end_time(self):
        return self.__dataset_end_time

    @property
    def selected_fields(self):
        return self.__selected_fields

    @property
    def hyper_params(self):
        return self.__hyper_params

    @property
    def target(self):
        return self.__target
