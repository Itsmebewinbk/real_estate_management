#!/bin/bash

APP_PORT=${APP_PORT:-8000}
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn moonhive_real_estate.wsgi:application -b 0.0.0.0:${
    APP_PORT} --timeout 300 --workers 4


