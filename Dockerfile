FROM python:3.8.5-alpine3.11

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "run"]
