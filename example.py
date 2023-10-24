import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from sdk.base import AlgoTemplate


class Example(AlgoTemplate):

    def build_model(self, hyper_params: dict) -> object:
        # get hyper params to build your model
        hello = hyper_params.get('hello')
        assert hello == 'world', 'hello world'
        model = KNeighborsClassifier()
        return model

    def train(self, model: KNeighborsClassifier, df: pd.DataFrame, hyper_params: dict) -> (object, dict):
        labels = np.random.randint(0, 1, size=(len(df), 1))
        model = model.fit(df, labels)
        return model, hyper_params

    def inference(self, model: KNeighborsClassifier, args: dict, x: pd.DataFrame) -> pd.Series:
        index = x.index
        return pd.Series(model.predict(x), index=index)


if __name__ == '__main__':
    # init  your model here
    Example()
