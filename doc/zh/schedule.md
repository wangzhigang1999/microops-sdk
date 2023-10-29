# Schedule

![image-20230903142607821](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230903142607821.png)

## 介绍

![image-20230911212238212](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230911212238212.png)

这里是对算法效果的验证。

通过前端页面启动一个实时异常检测的任务，监听来自Kafka的实时数据流并进行异常检测，将检测结果写入MongoDB中。在此过程中，可以通过[Chaos](doc/zh/chaos.md) 对你的Testbed进行干预如注入内存异常等，这些干预的效果会反映在实时的数据流中；如果算法的效果足够好，那么就能准确的捕获到这些异常。同时还可以根据注入的异常和检测出来的异常对算法的效果进行评估，计算P、R、F1指标。

## 使用

> 前置条件

必须有一个训练完的算法。

> 添加

添加一个检测任务，需要

1. 点击Add按钮。点击按钮之后，会弹出下图中央的对话框
2. 选择算法。 选择一个你需要部署的算法
3. 选择一个训练任务。当你在第二部选择了算法之后，平台会自动的帮你搜索对应的训练任务，这些训练任务的背后对应着一个个训练好的模型权重，在选择了训练任务之后，会自动匹配数据源
4. 设置对应的检测使用的超参数
5. 提交任务

![image-20230911213130909](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230911213130909.png)

> 使用

![image-20230911213550703](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230911213550703.png)

在成功的添加了一个任务之后，你应当能看到一条记录，如上图。 记录的最后对应着三个按钮：

1. Detail
2. Delete
3. Evaluation

Delete 会删掉当前的检测任务。

### Detail

![image-20230911214824125](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230911214824125.png)

Detail页面中如上图所示，包含着许多元素。下部的图表代表当前的实时数据源，两个固定指标pred和chaos，分别代表预测的异常区间和实际的异常注入区间。其余的指标均是在训练算法时选择的特征，如果在训练时没有选择，即使某个指标存在于数据源中，也不会显示出来。

在上图中，黄色的柱状图表示检测到了异常。

> **Start End Offset**

Start 代表图表显示的数据起始事件，End类似。

Offset 配合 End 可以决定 Start，常常用来监控最新几分钟的信息。

> AutoRefresh 和 Refresh Interval

控制是否开启自动刷新以及自动刷新的间隔，也可以选择手动刷新。

### Evaluation

![image-20230911214031668](https://wanz-bucket.oss-cn-beijing.aliyuncs.com/typora/image-20230911214031668.png)

Evaluation 负责评估当前算法的检测效果。

点击按钮后会弹出对话框，首选勾选需要计算的指标，然后选择事件范围计算即可。
