from abc import abstractmethod
from loguru import logger
import redis
from sdk.db.mongo_conn import MongoConnectClient

'''
example:
[
  {
    "storageType": "REDIS",
    "storageUsage": "model",
    "storageHost": "r-2zeq0rvmg07kxcxhsmpd.redis.rds.aliyuncs.com",
    "storagePort": 6379,
    "storagePassword": "zhigang911A",
    "storageProperties": {
      "db": 0
    }
  },
  {
    "storageType": "MONGO",
    "storageUsage": "result",
    "storageHost": "r-2zeq0rvmg07kxcxhsmpd.redis.rds.aliyuncs.com",
    "storagePort": 6379,
    "storagePassword": "zhigang911A",
    "storageProperties": {
      "db": "evaluation",
      "collection": "result"    
    }
  }
]
'''


class Storage:
    def __init__(self, config):
        self.type = config["type"]
        self.host = config["host"]
        self.port = config["port"]
        self.password = config["password"]
        self.properties = config["properties"]

    @abstractmethod
    def read(self, where):
        pass

    @abstractmethod
    def write(self, where, value):
        pass

