web: gunicorn web.wsgi --log-file -
worker: celery -A web worker --loglevel INFO
