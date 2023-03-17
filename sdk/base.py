from abc import abstractmethod
from datetime import datetime

import pandas as pd
from dateutil import tz
from loguru import logger

from sdk.config.config import Config


def parse_date(date_str):
    if isinstance(date_str, int):
        return date_str
    t = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=tz.tzutc())
    return int(t.timestamp())


class AlgoTemplate:
    def __init__(self):
        self.config = Config()
        self.model = None

        self.metric_map = self.__get_map()
        self.time_window = []
        self.metric_len = len(self.config.selected_fields)
        self.count = 0  # count number of metrics that met window_sz so that can give users the whole window
        self.first_run = True

        if self.config.mode == "TRAIN":
            self.model = self.build_model(self.config.hyper_params)
            self.__train()
        else:
            self.model, self.args = self.config.model_storage.load_model(self.config.model_path)
            self.__inference()

    def __train(self):
        logger.info("..............Starting training..............")

        logger.info("..............Loading data..............")
        # load data
        df = self.config.train_datasource.get_data(
            start_time=self.config.dataset_start_time,
            end_time=self.config.dataset_end_time,
            selected_fields=self.config.selected_fields
        )

        logger.info("..............Training model.............")
        # train model
        model, args = self.train(self.model, df, self.config.hyper_params)
        # store model
        logger.info("..............Storing model.............")
        self.config.model_storage.save_model(self.config.model_path, model, args)

    def __is_selected(self, metric):
        return metric["name"] in self.config.selected_fields

    def __get_map(self):
        initial_dict = {}
        for metric in self.config.selected_fields:
            initial_dict[metric] = pd.Series([], dtype=float)
        return initial_dict

    def __meet_size(self, series):
        return len(series) == self.config.hyper_params["window_size"]

    def __exceed_size(self, series):
        return len(series) > self.config.hyper_params["window_size"]

    def __all_meet_size(self):
        return self.count == self.metric_len

    def __load_window(self, message_value):
        metric_name = message_value['name']
        metric_value = message_value['value']
        metric_time = message_value['timestamp']
        self.metric_map[metric_name] = pd.concat(
            [self.metric_map[metric_name], pd.Series(metric_value, index=[parse_date(metric_time)])])

        if self.__meet_size(self.metric_map[metric_name]):
            self.count += 1
        elif self.__exceed_size(self.metric_map[metric_name]):
            logger.error("{} is collected faster".format(metric_name))

    def __window_pop(self):
        # update window
        for metric in self.config.selected_fields:
            self.metric_map[metric] = self.metric_map[metric].iloc[self.config.hyper_params["window_step"]:]
        # update time window
        self.time_window = self.time_window[self.config.hyper_params["window_step"]:]
        # clear count
        self.count = 0

    def __run_model(self):
        # get dataframe
        metric_series_list = [self.metric_map[metric] for metric in self.config.selected_fields]
        metric_df = pd.concat(metric_series_list, axis=1)
        metric_df.columns = self.config.selected_fields  # set column names after concat
        metric_df = metric_df.reindex(columns=sorted(metric_df.columns))  # order df columns
        # run model in window
        logger.info("window dataframe for inference:\n {}".format(metric_df))
        result_series = self.inference(self.model, self.args, metric_df)
        logger.info("inference result series:\n {}".format(result_series))
        # store result
        if self.first_run:
            self.config.result_storage.store_result(self.config.result_path, self.config.algorithm.get_name(),
                                                    self.config.dataset_start_time, self.config.dataset_end_time,
                                                    result_series)
            self.first_run = False
        else:
            self.config.result_storage.store_result(self.config.result_path, self.config.algorithm.get_name(),
                                                    self.config.dataset_start_time, self.config.dataset_end_time,
                                                    result_series[-self.config.hyper_params["window_step"]:])

    def __inference(self):
        logger.info("..............Starting inference..............")
        for message in self.config.inference_datasource.get_stream_handler():
            message_value = message.value
            message_value["value"] = float(message_value["value"])
            if self.__is_selected(message_value):
                logger.info("current message value is:\n {}".format(message_value))
                self.__load_window(message_value)
                if self.__all_meet_size():
                    self.__run_model()
                    self.__window_pop()

    @abstractmethod
    def build_model(self, hyper_params: dict) -> object:
        pass

    @abstractmethod
    def train(self, model: object, df: pd.DataFrame, hyper_params: dict) -> (object, dict):
        pass

    @abstractmethod
    def inference(self, model: object, args: dict, df: pd.DataFrame) -> pd.Series:
        pass
