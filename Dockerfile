FROM python:3.6.7

USER root

EXPOSE 8888

WORKDIR /code

COPY pip.conf /etc/pip.conf
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD uwsgi uwsgi.ini