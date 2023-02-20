from kafka import KafkaConsumer
from loguru import logger


class KafkaConfig:
    def __init__(self, host, port, properties=None, username=None, password=None):

        self.host = host
        self.port = port

        if properties is None:
            properties = {}
            self.topic = "default"
            logger.warning("No topic provided, using default topic: default")
        else:
            properties = properties
            self.topic = properties["topic"]

        self.bootstrap_servers = "{}:{}".format(self.host, self.port)
        self.username = username
        self.password = password
        self.properties = properties

        logger.info("KafkaConfig: {}".format(self.__dict__))
        self.kafka_consumer = KafkaConsumer(bootstrap_servers=self.bootstrap_servers, group_id=self.topic)
        self.kafka_consumer.subscribe([self.topic])

        logger.info("Kafka consumer created")

    def getKafkaConsumer(self):
        return self.kafka_consumer
