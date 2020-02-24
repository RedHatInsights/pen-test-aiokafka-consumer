FROM python:2.7

ADD . /pen-test-aiokafka-consumer
WORKDIR /pen-test-aiokafka-consumer

RUN pip install pipenv
RUN pipenv install --dev
RUN pipenv lock --requirements > requirements.txt
RUN pipenv run python consumer.py
