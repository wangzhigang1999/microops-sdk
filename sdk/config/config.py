import json
import os

from sdk.config.datasource import DataSource
from sdk.config.storage import Storage
from sdk.config.algorithm import Algorithm


class Config(object):

    def __init__(self):
        self.MODE = os.environ.get('MODE', 'TRAIN')

        self.json_config = json.loads(os.environ.get('CONFIG', '{}'))

        self.storage = Storage(self.json_config["storage"])
        self.algorithm = Algorithm(self.json_config["algorithm"])
        self.datasource = DataSource(self.json_config["datasource"])

        self.model_path = self.json_config["ModelPath"]

        self.hyper_parameters = self.json_config["HyperParams"]

    def getMode(self):
        return self.MODE

    def getStorage(self):
        return self.storage

    def getAlgorithm(self):
        return self.algorithm

    def getDataSource(self):
        return self.datasource

    def getModelPath(self):
        return self.model_path

    def getHyperParameters(self):
        return self.hyper_parameters
