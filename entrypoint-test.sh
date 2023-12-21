#!/bin/bash

until nc -z -v -w30 db 5432
do
  echo 'Waiting for database connection'
  sleep 5
done

python manage.py migrate

#python -m unittest discover
pytest .
