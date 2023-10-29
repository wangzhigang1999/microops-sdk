# Train

![image-20230903141134298](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230903141134298.png)

## 介绍

<img src="https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230903141402020.png" alt="image-20230903141402020" style="zoom:50%;" />

这里的训练和传统意义上的训练是**同样的概念**，都需要算法和数据源。算法参考[算法](doc/zn/model.md)章节的文档，数据集参考[这里](doc/zh/dataset.md)。

只需要在前端进行操作，即可下发训练任务，训练产物会被保存至Redis中。

## 使用

在Model这个标签下，点击 **Add** 按钮，可以进入下边的页面：

![image-20230903141836318](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230903141836318.png)

只需要：

1. 选择数据集
2. 选择算法
3. 调整训练字段和训练数据的范围
4. 调整超参数
5. 提交任务

即可提交一个训练任务。平台会启动一个训练的Pod根据你设置的参数进行训练，训练完成之后会将模型保存在Redis中。

> 数据集

你看可以看到所有的**属于你的**和**公开的**数据集。

![image-20230903142121155](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230903142121155.png)

> 算法

同样的，你可以看到属于你的和公开的算法。
