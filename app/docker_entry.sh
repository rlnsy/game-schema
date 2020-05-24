#!/bin/bash

./migrate.sh

python manage.py collectstatic

exec "$@"
