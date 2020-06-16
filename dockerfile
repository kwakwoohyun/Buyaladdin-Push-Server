# docker/DockFile
FROM python:3.7

RUN apt-get -y update

RUN mkdir /code
COPY requirements.txt /code
WORKDIR /code

ENV GOOGLE_APPLICATION_CREDENTIALS API-59a21c3115c7.json

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code