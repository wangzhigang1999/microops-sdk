import redis
from loguru import logger


class RedisConfig:
    def __init__(self, host, port, password, properties):
        self.host = host
        self.port = port
        self.db = properties["db"]
        self.password = password

        logger.info("RedisConfig: {}".format(self.__dict__))

        self.redis = redis.Redis(host=host, port=port, password=password, db=self.db)
        logger.info("Redis client created")

    def getRedisClient(self):
        return self.redis
