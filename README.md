# MicroOps SDK User Guide

## Introduction

Welcome to MicroOps SDK, a set of libraries designed for developing algorithms on the MicroOps platform. This platform is specially tailored for your algorithmic needs. It enables you to create and train your models with ease. When running, the MicroOps platform automatically sets up a "pod" to execute your code. You can use the `train` method to train your model and the `inference` method to test it. Hyperparameters are easily passed to your pod via **environment variables**, which can be accessed directly within the `train` and `inference` methods.

## Getting Started

### Cloning the Repository

First, clone our repository by running the following command:

```shell
git clone https://github.com/wangzhigang1999/microops-sdk.git
```

### Extending the `AlgoTemplate` Class

Once you've cloned the repository, you'll need to extend the `AlgoTemplate` class to create your own algorithm. Your custom algorithm should include the following three methods: `build_model`, `train`, and `inference`.

### Implementing the `build_model` Method

The `build_model` method is responsible for creating your model. You can access hyperparameters from the `hyper_params` parameter to customize your model. This method must return your model, as MicroOps will call it prior to training or inference.

### Implementing the `train` Method

The `train` method is used to train your model. MicroOps will provide the model you built using the `build_model` method and the training data in the form of a pandas DataFrame, which includes features and labels (if applicable). You can directly use the `model` parameter to access your model. In this method, you should implement your training logic and return both the trained model and hyperparameters.

### Implementing the `inference` Method

The `inference` method is designed for testing your model. MicroOps will pass the model trained with the `train` method and the test data, also in the form of a pandas DataFrame. The test data mirrors the features of the training data, complete with an index column representing timestamps. In this method, you should **return a pandas Series** containing predictions based on the test data. The index of the Series should match the index of the test data. MicroOps will save these predictions to the database, making them accessible on the MicroOps platform.

### Initializing Your Model in the `__main__` Method

Don't forget to initialize your model within the `__main__` method so that MicroOps can access it. Here's an example of how to do it:

```python
if __name__ == '__main__':
    # Initialize your model here
    Example()
```

### Dockerizing Your Algorithm and Uploading It to MicroOps

To make your algorithm accessible on MicroOps, you should containerize it using Docker and upload the container image to the platform. MicroOps will pull your algorithm image and run it. Follow these steps to add your algorithm:

1. Click the "Add" button.

2. Fill in the required information.

- **Name**: Provide a name for your algorithm.
- **Description**: Write a brief description of your algorithm.
- **URL**: Specify the URL of your algorithm image.
- **Hyperparameters**: Input your algorithm's hyperparameters in JSON format. You can also override them in MicroOps during training or inference.

## Example

Here's an example of how to create a custom algorithm using MicroOps SDK:

```python
class Example(AlgoTemplate):
    def build_model(self, hyper_params: dict) -> object:
        # Customize your model using hyperparameters
        hello = hyper_params.get('hello')
        assert hello == 'world', 'hello world'
        model = KNeighborsClassifier()
        return model

    def train(self, model: KNeighborsClassifier, df: pd.DataFrame, hyper_params: dict) -> (object, dict):
        # Implement your training logic
        labels = np.random.randint(0, 1, size=(len(df), 1))
        model = model.fit(df, labels)
        return model, hyper_params

    def inference(self, model: KNeighborsClassifier, hyper_params: dict, x: pd.DataFrame) -> pd.Series:
        # Perform inference and return predictions
        index = x.index
        return pd.Series(model.predict(x), index=index)

if __name__ == '__main__':
    # Initialize your model here
    Example()
```



Feel free to adapt this example to your specific needs and customize your algorithms for the MicroOps platform. **Happy coding!**