'''

example:

{
  "id": "63f320a11a1cf03bbd8f01c6",
  "name": "nginx",
  "description": "nginx",
  "author": "wanz",
  "version": "1.0",
  "url": "nginx",
  "type": "KNN",
  "command": "./main",
  "hashString": "1047602181047602183641878485631047602189941102701363690234"
}


'''


class Algorithm:
    def __init__(self, config):
        # self.id = self.json_config["id"]
        self.__name = config["name"]
        # self.description = self.json_config["description"]
        # self.author = self.json_config["author"]
        # self.version = self.json_config["version"]
        # self.url = self.json_config["url"]
        # self.__type = self.json_config["type"]
        # self.command = self.json_config["command"]
        # self.hashString = self.json_config["hashString"]

    def get_name(self):
        return self.__name
