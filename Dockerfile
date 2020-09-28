# pull official base image
FROM python:3.8-alpine

# Used to generate bulk data on heroku

# VOLUME /tmp
# RUN apk add --no-cache curl bash openssh python3
# ADD /heroku-exec.sh /app/.profile.d/heroku-exec.sh
# RUN chmod a+x /app/.profile.d/heroku-exec.sh

# ADD /sh-wrapper.sh /bin/sh-wrapper.sh
# RUN chmod a+x /bin/sh-wrapper.sh
# RUN rm /bin/sh && ln -s /bin/sh-wrapper.sh /bin/sh

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate --run-syncdb
RUN python manage.py setup
# RUN python manage.py bulkcreate

# add and run as non-root user
RUN adduser -D myuser
USER myuser


# run gunicorn
CMD gunicorn perpayBackend.wsgi:application --bind 0.0.0.0:$PORT