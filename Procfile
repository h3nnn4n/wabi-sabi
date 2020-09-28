release: python manage.py migrate
web: gunicorn web.wsgi --log-file -
worker: celery -A web worker --beat --loglevel INFO
