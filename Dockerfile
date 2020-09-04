FROM python:latest

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "run"]
