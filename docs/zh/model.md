# Model

## 介绍

Model 中包含着一系列的算法模型，比如DLinear、Transformer等等。

这些算法都根据我们的SDK进行了一些改造，以更方便的和我们的平台进行集成。

算法基于SDK开发后，会被打包成一个Docker容器，平台上只保留对应的容器的链接。比如`registry.cn-beijing.aliyuncs.com/nirc/ts-lib:latest`。除此之外，平台还会保存算法训练和推理所需要的一系列超参数。

在训练或者检测的时候，用户可以根据自己的需求对这些参数进行修改，以满足自己的需求。

如果你要开发自己的模型并将它集成到 MicroOps 中，请参考： [SDK使用文档](https://github.com/wangzhigang1999/microops-sdk)

## 使用

对于一个算法，可以选择[训练](docs/zh/train.md)或者[测试](docs/zh/schedule.md)。

具体请查看相应的章节。

## 添加

点击`ADD`按钮进入下面的页面，你需要填写下面的一些字段：

- 名称：为您的算法提供名称。

- 描述：您的算法的简要说明。

- URL：指定算法镜像的URL。

- 超参数：以JSON格式输入算法的超参数。

![image-20231029210802368](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20231029210802368.png)

输入完成点击提交即可。
