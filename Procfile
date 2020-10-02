release: python manage.py migrate
web: gunicorn web.wsgi --log-file -
flower: flower --port=$FLOWER_PORT --broker=$CLOUDAMQP_URL --basic_auth=$FLOWER_BASIC_AUTH
main_worker: celery -A web worker --beat --loglevel INFO
