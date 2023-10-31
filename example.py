import pandas as pd

from sdk.base import AlgoTemplate

from loguru import logger


class Example(AlgoTemplate):

    def build_model(self, hyper_params: dict) -> object:
        # get hyper params to build your model
        hello = hyper_params.get('hello')
        assert hello == 'world', 'hello world'

        # build your model here and return it
        return {"hello": hello}

    def train(self, model: dict, df: pd.DataFrame, hyper_params: dict) -> (object, dict):
        # calculate the mean and std of each feature
        for feature in df.columns:
            mean = df[feature].mean()
            std = df[feature].std()
            model[feature] = {'mean': mean, 'std': std}
        logger.info(f"model: {model}")

        return model, hyper_params

    def inference(self, model: dict, args: dict, x: pd.DataFrame) -> pd.Series:
        index = x.index

        result = []
        for feature in x.columns:
            mean = model[feature]['mean']
            std = model[feature]['std']

            # for each feature, using 3-sigma rule to filter the outliers
            x[feature] = x[feature].apply(lambda x: 0 if abs(x - mean) < 3 * std else 1)

        # for each row, if all features are 0, then it is a normal row, otherwise it is an outlier
        for _, row in x.iterrows():
            if row.sum() == 0:
                result.append(0)
            else:
                result.append(1)

        logger.info(f"result: {result}")

        return pd.Series(result, index=index)


if __name__ == '__main__':
    # init  your model here
    Example()
