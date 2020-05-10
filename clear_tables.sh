#!/bin/sh

./make_migrations.sh
python manage.py migrate games zero
python manage.py migrate game_dice zero
./migrate.sh
