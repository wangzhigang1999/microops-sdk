import json

from kafka import KafkaConsumer

from sdk.config.datasource.stream_datasource import StreamDataSource


class KafkaDataSource(StreamDataSource):
    def __init__(self, config):
        super(KafkaDataSource, self).__init__(config)
        self.topic_name = self.properties["topic"]
        self.group_id = self.properties["groupID"]
        self.bootstrap_server = self.host + ":" + str(self.port)
        self.consumer = KafkaConsumer(self.topic_name, group_id=self.group_id,
                                      bootstrap_servers=[self.bootstrap_server],
                                      auto_offset_reset='latest', enable_auto_commit=True,
                                      value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    def get_stream_handler(self):
        return self.consumer
