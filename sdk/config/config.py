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
        self.mode = os.environ.get('MODE', 'TRAIN')
        # logger.info("current mode is {}".format(self.mode))
        self.json_config = json.loads(os.environ.get('CONFIG', '{}'))

        self.model_path = self.json_config["modelPath"]
        self.result_path = self.json_config["resultPath"]

        self.__init_storage()
        self.__init_datasource()

        self.algorithm = Algorithm(self.json_config["algorithm"])
        self.dataset_start_time = self.json_config["datasetStartTime"]
        self.dataset_end_time = self.json_config["datasetEndTime"]
        self.selected_fields = self.json_config["selectedFields"]
        self.hyper_parameters = self.json_config["hyperParams"]

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

    def get_model_storage(self):
        return self.__model_storage

    def get_result_storage(self):
        return self.__result_storage

    def get_train_datasource(self):
        return self.__train_datasource

    def get_inference_datasource(self):
        return self.__inference_datasource
