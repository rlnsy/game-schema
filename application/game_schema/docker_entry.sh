#!/bin/sh

python manage.py makemigrations games
python manage.py makemigrations game_dice
python manage.py migrate

exec "$@"
