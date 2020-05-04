#!/bin/sh

echo "Applying database migrations"
./migrate.sh
echo "Running tests"
python manage.py test
