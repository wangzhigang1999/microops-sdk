# Chaos

## 故障实验列表

![chaos](assets/doc/img/chaos.png)

Chaos模块的首页由三个包含故障实验列表的tab子页面组成，其中：
- Experiments：展示了`单个故障实验`的历史记录。
- Schedules：展示了`定时故障实验`的历史记录。
- Archives：展示了归档后的Experiments和Schedules。

详细的实验类型与配置见[注入](/doc/zh/chaos.md#注入)部分的文档。

**注**：本模块仅向用户开放Kubernetes的服务故障注入，并不支持用户对底层物理机注入故障，这会威胁到其他用户资源与平台安全。

### Experiments

![chaos-experiments](assets/doc/img/chaos-experiments.png)

Experiments表格中有七列，其中：
1. Experiment Name：实验的名称，由平台根据`type-uid`的格式自动生成，`type`为注入的故障类型，`uid`为uuid生成的唯一标识符。
2. Kind：注入的故障种类，一个种类（kind）可能包含多个类型（type），这一字段即Chaos Mesh中的故障YAML文件的`Kind`字段值。
3. Target：故障注入的目标，平台仅允许Kubernetes的服务故障注入，表格展示的格式为`namespace.service`。
4. Start Time：故障注入的开始时间。
5. Duration：故障注入的持续时间。
6. Events：通过点击Events按钮，可以获取该故障实验最近的事件，了解实验的状态（通过watch异步监听实现）。
7. Ops：支持的用户操作，此处包含两个操作： 
   1. Reuse：通过点击Reuse按钮，可以查看该故障实验对应的YAML文件，再点击YES，即可复用该故障实验（实验名称平台会自动更换）。
   2. Archive：暂停并归档实验，归档后的实验将不会在历史记录的表格中出现。

### Schedules

![chaos-schedules](assets/doc/img/chaos-schedules.png)

Schedule是定时任务，可以在固定的时间（或根据固定的时间间隔）自动新建故障实验，表格中有四列，其中：
1. Schedule Name：定时故障任务的名称，同样由平台自动生成，格式为`schedule-type-uid`，`type`为注入的故障类型，`uid`为uuid生成的唯一标识符。
2. Start Time：定时故障任务的开始时间。由于定时任务不断执行，直到用户暂停/归档为止，因此Schedule并没有Duration字段。
3. Events：同Experiments中的Events，点击Events按钮可以获取定时故障实验的最近事件。尝试获取Schedule事件后可能会有以下错误信息：

> Failed to get run time: too many missed start time (> 100). Set or decrease .spec.startingDeadlineSeconds or check clock skew
  
其中`startingDeadlineSeconds`是[Cronjob](https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/cron-jobs/)中的概念，平台遵循默认的设置为`null`。
这一错误信息表示CronJob控制器检查到从上一个执行时间到现在，错过了超过100次应有的执行，它将不再执行该定时任务。这一般是用户长期暂停一个故障实验，再尝试继续该实验会产生的错误，用户只需点击Reuse重用该实验即可，原实验可以通过归档来丢弃。

4. Ops：Schedule支持三种操作，其中Reuse和Archive与Experiments中的对应操作是相同的。当Schedule定时任务开始后，Pause按钮允许用户暂停Schedule，这不仅仅会阻止它创建新的实验，也会暂停已创建的实验；暂停后，Resume按钮则可以解除暂停。

### Archives

![chaos-archives](assets/doc/img/chaos-archives.png)

Archives是归档后的故障实验，表格字段相同，不再赘述。但是操作略有不同，归档后的实验会在30天后会自动永久删除，用户也可以自行删除。

## 故障注入

 <img src="assets/doc/img/chaos-add.png" width = "800" height = "800" alt="chaos-add"/>

点击Chaos模块首页的Add按钮进入到故障注入的配置页面，在该页面用户可以选择故障类型、注入目标与定时的时间间隔。

### 故障类型
目前，我们提供了最常用的三种故障类型：
- [pod-failure](https://chaos-mesh.org/zh/docs/simulate-pod-chaos-on-kubernetes/#pod-failure-%E7%A4%BA%E4%BE%8B)：使得指定服务中的pod均不可用。
- [cpu-stress](https://chaos-mesh.org/zh/docs/simulate-heavy-stress-on-kubernetes/)：模拟指定服务中容器的CPU压力。
- [memory-stress](https://chaos-mesh.org/zh/docs/simulate-heavy-stress-on-kubernetes/): 模拟指定服务中容器的内存压力。

在选择故障类型后，该故障需要填写的字段就会出现在下方，根据输入框的提示输入即可。 

### 注入目标
用户只能向自己创建的testbed中的服务注入故障，注入页面提供了用户所有testbed以及对应所有服务的下拉列表供选择。

### Schedule

默认注入的是单个故障实验，定时任务开关默认关闭。 若想注入定时的故障实验，则可以打开Schedule的开关，按要求填写[Cronjob格式](https://crontab.guru/)的内容来描述定时任务。

最终点击页面底部的Submit按钮即可提交故障注入实验，页面会自动跳转到Chaos模块的首页，方便查看实验的状态。
