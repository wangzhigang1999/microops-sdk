import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from sdk.base import AlgoTemplate


class Example(AlgoTemplate):

    def build_model(self, hyper_params: dict) -> object:
        # knn
        hello = hyper_params.get('hello')
        assert hello == 'world', 'hello world'
        model = KNeighborsClassifier()
        return model

    def train(self, model: KNeighborsClassifier, df: pd.DataFrame, hyper_params: dict) -> (object, dict):
        labels = np.random.randint(0, 2, size=(len(df), 1))
        model = model.fit(df, labels)
        return model, hyper_params

    def inference(self, model: KNeighborsClassifier, args: dict, df: pd.DataFrame) -> pd.Series:
        return pd.Series(model.predict(df))


if __name__ == '__main__':
    Example()
