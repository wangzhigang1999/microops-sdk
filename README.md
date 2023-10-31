

![image-20231029204256689](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20231029204256689.png)

## 概念介绍

### Benchmark

一个用于基准测试的微服务系统被称为benchmark，在 MicroOps 中以Yaml文件的形式维护。

Benchmark 模块负责基准微服务部署文件的托管，集成了用户上传的微服务部署脚本与相关介绍，用户可以管理自己的benchmark、查看与下载他人公开的benchmark，以及部署benchmark以创建一个testbed。

### Testbed

一个运行的benchmark微服务系统被称为一个testbed，提供了实验与测试的环境。

Testbed模块负责用户testbed的托管，用户可以查看并管理自己部署的testbed，还可以补充部署用户流量模拟。

**MicroOps 中的所有操作都是围绕 Testbed 展开的。**

### Dataset

Dataset 是可用的一些数据集,你可以在MicroOps中浏览和使用这些数据集。

## 快速开始

> 快速部署一个 testbed 👇

<iframe src="https://scribehow.com/embed/_testbed__PNLCuVhDTLCmuoKfd2qROg" width="100%" height="640" allowfullscreen frameborder="0"></iframe>

> 浏览生成的数据集

<iframe src="https://scribehow.com/embed/__CuHwPMNVTw6Ys-j-sG-2ZQ" width="100%" height="640" allowfullscreen frameborder="0"></iframe>

> 使用某个数据集对某个算法进行训练 👇

<iframe src="https://scribehow.com/embed/__ShCSGQHBSBOQL-ECnLwvGA" width="100%" height="640" allowfullscreen frameborder="0"></iframe>

> 启动一个实时任务 👇

<iframe src="https://scribehow.com/embed/__TNd-KKbXS_ODX6ELPxGCkw" width="100%" height="640" allowfullscreen frameborder="0"></iframe>


> 异常注入 👇

<iframe src="https://scribehow.com/embed/__5Z7FoSleT4yAq0Lxml1uxg" width="100%" height="640" allowfullscreen frameborder="0"></iframe>

## 详细文档

 -    [Benchmark](docs/zh/benchmark.md)
-  [Testbed](docs/zh/testbed.md)
-  [Dataset](docs/zh/dataset.md)
-  [Train](docs/zh/train.md)
-  [Test](docs/zh/schedule.md)
-  [Chaos](docs/zh/chaos.md)
