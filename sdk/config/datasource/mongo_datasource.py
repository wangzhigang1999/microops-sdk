import pandas as pd
from loguru import logger

from sdk.config.datasource.batch_datasource import BatchDataSource
from sdk.db.mongo_conn import MongoConnectClient


class MongoDataSource(BatchDataSource):
    def __init__(self, config):
        super(MongoDataSource, self).__init__(config)
        self.client = MongoConnectClient(host=self.host,
                                         port=self.port,
                                         username=self.username,
                                         password=self.password)
        self.db = self.properties["db"]
        self.collection = self.properties["collection"]
        self.default_projected_fields = {"timestamp": 1, "_id": 0}
        self.default_df_index = "timestamp"

    def get_default_projected_fields(self):
        return self.default_projected_fields

    def set_default_projected_fields(self, projects: dict):
        self.default_projected_fields = projects

    def get_default_df_index(self):
        return self.default_df_index

    def set_default_df_index(self, index: str):
        self.default_df_index = index

    def get_data(self, start_time: int, end_time: int, selected_fields: list) -> pd.DataFrame:
        projects = self.default_projected_fields
        for field in selected_fields:
            projects[field] = 1

        query = {}
        if start_time != -1:
            query["start_time"] = {"$gte": start_time}
        if end_time != -1:
            query["end_time"] = {"$lte": end_time}

        records = self.client.get_all(self.db, self.collection, query=query, projects=projects)

        df = pd.DataFrame(list(records))
        df = df.set_index(self.default_df_index)
        logger.info("get train data dataframe, head is : {}".format(df.head()))
        return df
