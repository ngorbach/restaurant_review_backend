#!/bin/bash
python manage.py migrate --fake
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
#python manage.py collectstatic
gunicorn -w 4 -b 0.0.0.0:8000 app.wsgi:application
#python manage runserver 0.0.0.0:8000
