FROM python:3.8.6-buster

RUN apt update
RUN alias py=python

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/

COPY ./apps ./apps
COPY ./kinostats ./kinostats
COPY manage.py .
COPY ./requirements.txt .
COPY ./media ./media
COPY ./static ./static

RUN pip install -r requirements.txt


EXPOSE 443

CMD python manage.py runserver 0.0.0.0:443