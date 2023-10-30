import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from sdk.base import AlgoTemplate

from loguru import logger


class Example(AlgoTemplate):

    def build_model(self, hyper_params: dict) -> object:
        # get hyper params to build your model
        hello = hyper_params.get('hello')
        assert hello == 'world', 'hello world'
        # 3-sigma rule
        return "Your model object"

    def train(self, model: KNeighborsClassifier, df: pd.DataFrame, hyper_params: dict) -> (object, dict):
        return model, hyper_params

    def inference(self, model: KNeighborsClassifier, args: dict, x: pd.DataFrame) -> pd.Series:
        index = x.index

        # for each feature,we calculate 3-sigma rule
        # if the value is out of 3-sigma rule,we set it to 0
        for feature in x.columns:
            mean = x[feature].mean()
            std = x[feature].std()
            x[feature] = x[feature].apply(lambda x: 1 if x > mean + 3 * std or x < mean - 3 * std else 0)

        # if any feature is 1,we set the result to 1
        result = x.apply(lambda x: 1 if x.any() else 0, axis=1)

        logger.info("inference result series:\n {}".format(result))

        return pd.Series(result, index=index)


if __name__ == '__main__':
    # init  your model here
    Example()
