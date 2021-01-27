FROM python:3.7-slim

EXPOSE 5000

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install --default-timeout=100 -r requirements.txt -i https://pypi.douban.com/simple

COPY . /app
