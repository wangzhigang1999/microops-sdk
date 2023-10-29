# Microops

这里是对不同模块的简要介绍，详细的使用方式可以点击对应的标题查看。

![image-20230903141306202](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230903141306202.png)

## [Benchmark](doc/zh/benchmark.md)

一个用于基准测试的微服务系统被称为benchmark，在本平台中以部署文件的形式维护。Benchmark模块负责基准微服务部署文件的托管，集成了用户上传的微服务部署脚本与相关介绍，用户可以管理自己的benchmark、查看与下载他人公开的benchmark，
以及部署benchmark以创建一个testbed。

 <img src="assets/doc/img/benchmark.png" width = "1000" height = "1000" alt="benchmark" align=center />

[//]: # (![image-20230901112936005]&#40;https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230901112936005.png&#41;)

## [Testbed](doc/zh/testbed.md)

一个运行的benchmark微服务系统被称为一个testbed，提供了实验与测试的环境。Testbed模块负责用户testbed的托管，用户可以查看并管理自己部署的testbed，还可以补充部署用户流量模拟。

![image-20230901113002036](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230901113002036.png)

## [Model](doc/zh/model.md)

Model 代表着的算法。

![image-20230901113015481](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230901113015481.png)

## [Dataset](doc/zh/dataset.md)

Dataset 是可用的一些数据集。

![image-20230901113030512](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230901113030512.png)

## [Train](doc/zh/train.md)

使用某个数据集对某个算法进行训练。

![image-20230901113044442](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230901113044442.png)

## [Schedule](doc/zh/schedule.md)

对于一个训练后的算法，我们可以将其接入某个实时的数据源，对这个数据源进行实时的异常检测等。

![image-20230901113059392](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230901113059392.png)

## [Chaos](doc/zh/chaos.md)

Chaos模块是依托[Chaos Mesh](https://chaos-mesh.org/website-zh/)混沌工程平台的故障注入面板，允许用户选择其部署的某个Testbed的某个服务进行故障注入，
达到测试、生产数据等目标。

![testbed](assets/doc/img/testbed.png)

[//]: # (![image-20230901113118173]&#40;https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230901113118173.png&#41;)
