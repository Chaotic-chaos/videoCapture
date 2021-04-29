FROM python:3.8

MAINTAINER Chaos life0531@foxmail.com

WORKDIR /app
COPY . /app

RUN pip install  -r requirements.txt -i https://pypi.douban.com/simple
RUN pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python

CMD ["python3", "manage.py", "runserver", "0.0.0.0:1111"]








