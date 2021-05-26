import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)
    print(config)

def create_knime_api_docker_file(config=config):
    knime_api_docker = """# syntax=docker/dockerfile:1
    FROM ubuntu:18.04
    ENV DOWNLOAD_URL """+config["knime_download_url"]+"""
    ENV INSTALLATION_DIR /app
    RUN mkdir app
    RUN apt-get update -y
    RUN apt-get install -y python3.6 python3-pip
    RUN apt-get install -y default-jre curl
    RUN apt-get install -y wget
    RUN apt-get install -y unzip
    COPY . /app
    RUN wget """+config["knime_workflow_download_url"]+"""
    RUN unzip """+config["knime_workflow_file_name"]+""" -d app
    RUN curl -L "$DOWNLOAD_URL" | tar vxz -C $INSTALLATION_DIR
    RUN pip3 install -r app/requirements.txt
    CMD python3 app/app.py"""

    with open("Dockerfile", "w") as knime_api_docker_file:
        knime_api_docker_file.write(knime_api_docker)

if __name__ == '__main__':
    create_knime_api_docker_file()
