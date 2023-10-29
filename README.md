#  MicroOps 

![image-20231029204256689](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20231029204256689.png)

**点击下面的标题，查看详细的介绍。**

## [Benchmark](docs/zh/benchmark.md)

一个用于基准测试的微服务系统被称为benchmark，在 MicroOps 中以部署文件的形式维护。

Benchmark 模块负责基准微服务部署文件的托管，集成了用户上传的微服务部署脚本与相关介绍，用户可以管理自己的benchmark、查看与下载他人公开的benchmark，

以及部署benchmark以创建一个testbed。

## [Testbed](docs/zh/testbed.md)

一个运行的benchmark微服务系统被称为一个testbed，提供了实验与测试的环境。

Testbed模块负责用户testbed的托管，用户可以查看并管理自己部署的testbed，还可以补充部署用户流量模拟。

> 快速部署一个 testbed 👇

<iframe src="https://scribehow.com/embed/_testbed__PNLCuVhDTLCmuoKfd2qROg" width="100%" height="640" allowfullscreen frameborder="0"></iframe>

## [Dataset](docs/zh/dataset.md)

Dataset 是可用的一些数据集,你可以在MicroOps中浏览和使用这些数据集。

> 如何使用数据集 👇

<iframe src="https://scribehow.com/embed/__CuHwPMNVTw6Ys-j-sG-2ZQ" width="100%" height="640" allowfullscreen frameborder="0"></iframe>

## [Train](docs/zh/train.md)

> 使用某个数据集对某个算法进行训练 👇

<iframe src="https://scribehow.com/embed/__ShCSGQHBSBOQL-ECnLwvGA" width="100%" height="640" allowfullscreen frameborder="0"></iframe>

## [Test](docs/zh/schedule.md)

对于一个训练后的算法，我们可以将其接入某个实时的数据源，对这个数据源进行实时的异常检测等。

> 启动一个实时任务 👇

<iframe src="https://scribehow.com/embed/__5Z7FoSleT4yAq0Lxml1uxg" width="100%" height="640" allowfullscreen frameborder="0"></iframe>

## [Chaos](docs/zh/chaos.md)

Chaos模块是依托[Chaos Mesh](https://chaos-mesh.org/website-zh/)混沌工程平台的故障注入面板，允许用户选择其部署的某个Testbed的某个服务进行故障注入，
达到测试、生产数据等目标。

> 异常注入 👇

<iframe src="https://scribehow.com/embed/__5Z7FoSleT4yAq0Lxml1uxg" width="100%" height="640" allowfullscreen frameborder="0"></iframe>