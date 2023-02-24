from abc import abstractmethod

from sdk.config.datasource.datasource import DataSource


class StreamDataSource(DataSource):
    def __init__(self, config):
        super(StreamDataSource, self).__init__(config)

    @abstractmethod
    def get_stream_handler(self):
        pass
