FROM python:3.9.13-buster
#FROM python:3.11.2-alpine3.16

WORKDIR /root

COPY . .

#RUN pip install -r req.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r req.txt

#ENV MODE=inference
#ENV SCHEDULE_CONFIG=[{"type":"KAFKA","name":"Kafka Topic: node_metrics","host":"192.168.31.197","port":9092,"username":"","password":"","properties":{"topic":"node_metrics"}},{"type":"REDIS","name":"Redis","host":"k8s.personai.cn","port":30566,"username":"","password":"","properties":{"db":0}},{"type":"JOB","model_name":"hello"}]

CMD ["python","algo-knn.py"]