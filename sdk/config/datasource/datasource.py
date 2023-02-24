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
        self.type = config["type"]
        self.host = config["host"]
        self.port = config["port"]
        self.username = config["username"]
        self.password = config["password"]
        self.properties = config["properties"]

