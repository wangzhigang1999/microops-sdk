# Testbed


## Testbed列表

![testbed](assets/doc/img/testbed.png)

Testbed模块首页由一个Add按钮和一个包含用户testbed相关信息的表格组成，点击Add按钮将跳转到Benchmark模块首页，而表格有四列，其中：
1. Name： 用户对testbed的命名，是一个超链接，可以点击跳转到testbed的[详情页](/doc/zh/testbed.md#详情页)。
2. Benchmark：testbed使用的微服务系统名称，以`email/name`的形式给出，其中`email`是benchmark的拥有者,`name`是benchmark的名称。
3. Namespace：testbed在Kubernetes中所属的命名空间，由平台自动创建。
4. Ops：支持的用户操作，此处包含两个操作：
   1. 流量模拟：如果用户上传的benchmark文件中包含流量模拟的YAML文件，则可以部署或者删除流量模拟。
   2. 删除testbed：删除testbed的所有资源，包括微服务系统以及流量模拟。

## Testbed详情

详情页由三个tab子页面构成，分别为Pods、Services和Ingresses。

### Pods

![testbed-pods](assets/doc/img/testbed-pods.png)

通过watch异步监控，每秒刷新当前testbed中各pod的状态，表格有四列，其中：
1. Name: pod名称，由Kubernetes生成。
2. Phase：pod的阶段，也就是在[生命周期](https://kubernetes.io/zh-cn/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase)中所处的位置。
3. Ready：pod是否就绪。
4. Message：人类可读的消息，给出pod状态转换的详细信息。

### Services

![testbed-services](assets/doc/img/testbed-services.png)

获取testbed中所创建服务的信息，基本就是用户上传的YAML文件中所确定的内容。表格有四列，其中：
1. Name：service名称，用户在benchmark的YAML文件中指定。
2. Namespace：service所在命名空间，也就是testbed所在命名空间。
3. Labels：用户在YAML文件中为服务添加的标签。
4. Ports：服务暴露的端口。
5. Type：服务的类型，决定服务如何在网络中暴露。

### Ingresses

![testbed-ingresses](assets/doc/img/testbed-ingresses.png)

包含一个Add按钮以及一个你已添加的ingress的表格。

点击Add按钮选择你希望添加ingress的服务以及对应端口，平台会创建一个ingress，并给出访问URL，使用该URL你就可以访问对应服务了。一般用于访问微服务的前端或流量模拟的前端。
