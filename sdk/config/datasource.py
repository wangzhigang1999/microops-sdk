from abc import abstractmethod

'''

example config:

{
  "id": "63f31dc6931bc864c30a990c",
  "type": "KAFKA",
  "name": "node_metrics",
  "host": "192.168.31.197",
  "port": 9092,
  "username": "",
  "password": "",
  "properties": {
    "topic": "node_metrics",
    "fields": [
      "cpu",
      "memory",
      "disk",
      "network"
    ]
  }
}

'''


class DataSource:
    def __init__(self, config):
        self.json_config = config

        self.id = self.json_config["id"]
        self.type = self.json_config["type"]
        self.name = self.json_config["name"]
        self.host = self.json_config["host"]
        self.port = self.json_config["port"]
        self.username = self.json_config["username"]
        self.password = self.json_config["password"]
        self.properties = self.json_config["properties"]

    @abstractmethod
    def load_train_data(self, **kwargs):
        pass
