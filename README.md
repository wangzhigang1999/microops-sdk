# Microops

这里是对不同模块的简要介绍，详细的使用方式可以点击对应的标题查看。

![image-20230903141306202](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230903141306202.png)

## [Benchmark](docs/zh/benchmark.md)

一个用于基准测试的微服务系统被称为benchmark，在本平台中以部署文件的形式维护。Benchmark模块负责基准微服务部署文件的托管，集成了用户上传的微服务部署脚本与相关介绍，用户可以管理自己的benchmark、查看与下载他人公开的benchmark，
以及部署benchmark以创建一个testbed。

## [Testbed](docs/zh/testbed.md)

一个运行的benchmark微服务系统被称为一个testbed，提供了实验与测试的环境。Testbed模块负责用户testbed的托管，用户可以查看并管理自己部署的testbed，还可以补充部署用户流量模拟。

## [Model](docs/zh/model.md)

Model 代表着的算法。

## [Dataset](docs/zh/dataset.md)

Dataset 是可用的一些数据集。

## [Train](docs/zh/train.md)

使用某个数据集对某个算法进行训练。

## [Schedule](docs/zh/schedule.md)

对于一个训练后的算法，我们可以将其接入某个实时的数据源，对这个数据源进行实时的异常检测等。

## [Chaos](docs/zh/chaos.md)

Chaos模块是依托[Chaos Mesh](https://chaos-mesh.org/website-zh/)混沌工程平台的故障注入面板，允许用户选择其部署的某个Testbed的某个服务进行故障注入，
达到测试、生产数据等目标。
