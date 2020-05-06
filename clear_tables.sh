#!/bin/sh

python manage.py migrate games zero
python manage.py migrate game_dice zero
./migrate.sh
