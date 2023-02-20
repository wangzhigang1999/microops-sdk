from redis.client import Redis

from sdk.config.kafka_config import KafkaConfig
from sdk.config.redis_config import RedisConfig


class InferenceConfig:
    def __init__(self, model_name=None, kafkaConfig: KafkaConfig = None, redisConfig: RedisConfig = None):
        self.redisConfig = redisConfig
        self.kafkaConfig = kafkaConfig
        self.model_name = model_name

    def getRedisClient(self) -> Redis:
        return self.redisConfig.getRedisClient()

    def getKafkaClient(self):
        return self.kafkaConfig.getKafkaConsumer()

    def getModelName(self):
        return self.model_name
