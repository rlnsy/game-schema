#!/bin/sh

./make_migrations.sh
python manage.py migrate
