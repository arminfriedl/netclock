FROM python:3.8-alpine

RUN apk update && apk add redis su-exec \
  && pip3 install pipenv

COPY . /app
WORKDIR /app

ENV FLASK_APP=netclock.py
ENV FLASK_ENV=production

RUN pipenv install

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
