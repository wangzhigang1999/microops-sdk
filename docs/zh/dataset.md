# Dataset

![image-20230901113030512](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230901113030512.png)

## 介绍

Dataset 中包含着一些dataset，这些dataset都是平台自动收集而来的。目前**对用户自定义数据集的支持还不是很好**。

在[Testbed](doc/zh/testbed.md)这一节中，我们介绍了关于Testbed的相关细节，如果你还没有看过，可以先了解一下。

创建完一个Testbed之后，会存在着许许多多的服务，这些服务又是由一个一个的容器组成的。

平台会自动的收集并处理这些服务和容器的各种指标，然后将这些数据按照Testbed进行汇总。

你只能看到**属于你自己的和公共**的数据集。

如下图所示，包含着两个Namespace： **default** 和 **online-boutique-d6028f48-16d8-4099**； 在 **default** 这个Namespace中包含的都是公开的一些数据集，如节点的各种Metric；在 **online-boutique-d6028f48-16d8-4099** 这个Namespace中包含着其他一些数据集，这些数据集都是属于当前登录的用户的，只有当前的用户可见。

![image-20230902104244345](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230902104244345.png)

![image-20230902104316239](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230902104316239.png)

## 使用

> 预览

![image-20231029210442769](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20231029210442769.png)

> 下载

点击下载，可以以`CSV`的格式把数据集下载到本地使用
