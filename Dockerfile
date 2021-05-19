# syntax=docker/dockerfile:1
FROM ubuntu:18.04

ENV DOWNLOAD_URL https://download.knime.org/analytics-platform/linux/knime_4.1.0.linux.gtk.x86_64.tar.gz

ENV INSTALLATION_DIR /app

RUN mkdir app

RUN apt-get update -y

RUN apt-get install -y python3.6 python3-pip

RUN apt-get install -y default-jre curl

RUN apt-get install -y wget

RUN apt-get install -y unzip

COPY . /app

RUN wget https://github.com/gokhangerdan/knime_workflows/blob/main/knimepy.knwf?raw=true

RUN unzip knimepy.knwf?raw=true -d app

RUN curl -L "$DOWNLOAD_URL" | tar vxz -C $INSTALLATION_DIR

RUN pip3 install -r app/requirements.txt

RUN pip3 install knime

CMD python3 app/app.py
