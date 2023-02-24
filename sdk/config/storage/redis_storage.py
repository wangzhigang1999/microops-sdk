import pickle

import redis
from loguru import logger
from sdk.config.storage.storage import Storage


class RedisStorage(Storage):
    def __init__(self, config):
        super(RedisStorage, self).__init__(config)
        self.client = redis.Redis(host=self.host,
                                  port=self.port,
                                  password=self.password,
                                  db=self.properties["db"])

    def read(self, where):
        return pickle.loads(self.client.get(where))

    def write(self, where, value):
        self.client.set(where, pickle.dumps(value))
