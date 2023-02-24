from abc import abstractmethod

import pandas as pd

from sdk.config.datasource.datasource import DataSource


class BatchDataSource(DataSource):
    def __init__(self, config):
        super(BatchDataSource, self).__init__(config)

    @abstractmethod
    def get_data(self, start_time: int, end_time: int, selected_fields: list) -> pd.DataFrame:
        pass
