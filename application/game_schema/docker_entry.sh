#!/bin/sh

python manage.py makemigrations games
python manage.py migrate

exec "$@"
