# Model

![image-20230903100252326](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230903100252326.png)

## 介绍

Model 中包含着一系列的算法模型，比如DLinear、Transformer等等。

这些算法都根据我们的SDK进行了一些改造，以更方便的和我们的平台进行集成。由于目前SDK还不稳定，因此暂不开放。

算法基于SDK开发后，会被打包成一个Docker容器，平台上只保留对应的容器的链接。比如`registry.cn-beijing.aliyuncs.com/nirc/ts-lib:latest`。除此之外，平台还会保存算法训练和推理所需要的一系列超参数。

在训练或者检测的时候，用户可以根据自己的需求对这些参数进行修改，以满足自己的需求。

## 使用

对于一个算法，可以选择[训练](doc/zh/train.md)或者[部署](doc/zh/schedule.md)。

具体请查看相应的章节。
