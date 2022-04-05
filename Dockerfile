FROM python:3.9

WORKDIR /opt

COPY ./requirements.txt /opt/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt

COPY ./coalesce /opt/coalesce
