FROM python:3.9.13-buster
#FROM python:3.11.2-alpine3.16

WORKDIR /root

COPY . .

#RUN pip install -r req.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r req.txt


CMD ["python","example.py"]