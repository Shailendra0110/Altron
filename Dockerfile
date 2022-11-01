FROM python:3.9.7-slim-buster

RUN apt-get update && apt-get upgrade -y

RUN apt-get install git curl python3-pip ffmpeg -y

RUN pip3 install -U pip

COPY . /app/

WORKDIR /app/

RUN pip3 install -U -r requirements.txt

CMD python3 -m altron
