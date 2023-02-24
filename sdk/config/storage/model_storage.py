import json
import pickle

from sdk.config.storage.storage import Storage


class ModelStorage:
    def __init__(self, storage: Storage):
        self.storage = storage

    def load_model(self, model_path: str):
        data = self.storage.read(model_path)
        return data["model"], data["args"]

    def save_model(self, model_path: str, model: object, args: dict):
        self.storage.write(model_path, {"model": model, "args": args})
