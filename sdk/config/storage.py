from abc import abstractmethod


class Storage:
    def __init__(self, config):
        self.json_config = config

    @abstractmethod
    def store_model(self, model, model_path: str, **kwargs):
        pass

    @abstractmethod
    def load_model(self, model_path: str, **kwargs):
        pass
