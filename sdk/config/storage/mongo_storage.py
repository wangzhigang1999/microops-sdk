import redis
from loguru import logger
from sdk.config.storage.storage import Storage
from sdk.db.mongo_conn import MongoConnectClient


class MongoStorage(Storage):
    def __init__(self, config):
        super(MongoStorage, self).__init__(config)
        self.username = config["username"]  # TODO username是否应该在properties中？因为redis不需要username
        self.client = MongoConnectClient(host=self.host,
                                         port=self.port,
                                         username=self.username,
                                         password=self.password)
        self.db = self.properties["db"]

    def read(self, where):
        return self.client.get_all(self.db, where)

    def write(self, where, value):
        self.client.insert_one(self.db, where, value)
