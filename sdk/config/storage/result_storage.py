import pandas as pd

from sdk.config.storage.storage import Storage


class ResultStorage:
    def __init__(self, storage: Storage):
        self.storage = storage

    def store_result(self, result_path: str, algorithm: str, metrics: list, target_list: list, result: pd.Series):
        for index, value in result.items():
            self.storage.write(result_path, {
                "timestamp": index,
                "algorithm": algorithm,
                "metrics": metrics,
                "target_list": target_list,
                "predicted": value,
            })
