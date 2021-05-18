# syntax=docker/dockerfile:1
FROM ubuntu:18.04

ENV DOWNLOAD_URL https://download.knime.org/analytics-platform/linux/knime_4.1.0.linux.gtk.x86_64.tar.gz

ENV INSTALLATION_DIR /app

RUN mkdir app

RUN apt-get update -y

RUN apt-get install -y python3.6 python3-pip

RUN apt-get install -y default-jre curl

COPY . /app

RUN curl -L "$DOWNLOAD_URL" | tar vxz -C $INSTALLATION_DIR

RUN pip3 install -r app/requirements.txt

RUN pip3 install knime

EXPOSE 8081

CMD python3 app/app.py
