FROM python:3.6
MAINTAINER konsond@gmail.com

COPY ./mysite /mysite

WORKDIR /mysite

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


