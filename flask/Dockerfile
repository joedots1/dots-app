FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install -y gcc libc-dev 

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]

