import time

from pyod.models.knn import KNN as knn
from loguru import logger

from sdk.base import AlgoTemplate


class KNN(AlgoTemplate):

    def build_model(self):
        super().build_model()

        if self.model is None:
            self.model = knn()

    def inference(self):
        kafka = self.inference_config.getKafkaClient()
        logger.info("Start inference")
        for msg in kafka:
            logger.info("Inference: {}".format(msg.value))
            value = self.predict(msg.value)
            logger.info("Inference result: {}".format(value))

    def __init__(self):
        super().__init__()
        self.modelType = "KNN"
        self.description = "KNN"

    def predict(self, x):
        return self.model.predict(x)

    def train_model(self, frame) -> object:
        logger.info("Training model")
        s = time.time()
        self.model.fit(frame.values.reshape(-1, 1))
        logger.info("Model trained,Time cost: {}".format(time.time() - s))
        return self.model


if __name__ == '__main__':
    algo = KNN()
    algo.start()


