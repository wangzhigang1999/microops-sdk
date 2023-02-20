from loguru import logger

from sdk.config.mongo_config import MongoConfig
from sdk.config.redis_config import RedisConfig


class TrainConfig:
    def __init__(self, model_name=None, mongo_config: MongoConfig = None, redis_config: RedisConfig = None):
        self.mongo = mongo_config
        self.redis = redis_config
        self.model_name = model_name
        logger.info("TrainConfig init success")

    def getMongoClient(self):
        return self.mongo.getMongoClient()

    def getRedisClient(self):
        return self.redis.getRedisClient()

    def getModelName(self):
        return self.model_name
