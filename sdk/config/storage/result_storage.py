import pandas as pd

from sdk.config.storage.storage import Storage

from loguru import logger


class ResultStorage:
    def __init__(self, storage: Storage):
        self.storage = storage

    def store_result(self, result_path: str, algorithm: str, metrics: list, target_list: list, result: pd.Series):
        logger.info("..............Storing result.............")
        for index, value in result.items():
            logger.info("Storing result for timestamp: {}".format(index))
            logger.info("Result: {}".format(value))
            logger.info("Metrics: {}".format(metrics))
            logger.info("Target list: {}".format(target_list))

            self.storage.write(result_path, {
                "timestamp": index,
                "algorithm": algorithm,
                "metrics": metrics,
                "target_list": target_list,
                "predicted": value,
            })
