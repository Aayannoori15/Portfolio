#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
    python manage.py createsuperuser --noinput || true
fi

gunicorn personalweb.wsgi
