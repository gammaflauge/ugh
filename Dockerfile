FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app/requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY ./app /app

