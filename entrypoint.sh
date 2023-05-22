#!/bin/sh
sleep 15
python manage.py migrate --no-input
python manage.py add_cities

exec "$@"