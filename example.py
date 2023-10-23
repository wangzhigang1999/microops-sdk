import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from sdk.base import AlgoTemplate


class Example(AlgoTemplate):

    def build_model(self, hyper_params: dict) -> object:
        # knn
        model = KNeighborsClassifier()
        return model

    def train(self, model: KNeighborsClassifier, df: pd.DataFrame, hyper_params: dict) -> (object, dict):
        model = model.fit(df, 0)
        return model, hyper_params

    def inference(self, model: KNeighborsClassifier, args: dict, df: pd.DataFrame) -> pd.Series:
        return pd.Series(model.predict(df))


if __name__ == '__main__':
    Example()
