from loguru import logger

from sdk.db.mongo_conn import MongoConnectClient


class MongoConfig:
    def __init__(self, host, port, username, password, properties):
        self.host = host
        self.port = port
        self.db = properties["db"]
        self.collection = properties["collection"]

        self.username = username
        self.password = password

        self.start_time = properties["start_time"]
        self.end_time = properties["end_time"]

        logger.info("MongoConfig: {}", self.__dict__)
        self.client = MongoConnectClient(self.host, self.port, username, password)

        logger.info("MongoClient created")

    def getMongoClient(self):
        return self.client
