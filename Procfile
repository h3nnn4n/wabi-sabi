release: python manage.py migrate
web: gunicorn web.wsgi --log-file -
main_worker: celery -A web worker --beat --loglevel INFO
