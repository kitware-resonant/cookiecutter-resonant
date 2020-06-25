release: ./manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT girder.wsgi
worker: REMAP_SIGTERM=SIGQUIT celery worker --app girder.celery --loglevel info --without-heartbeat
beat: REMAP_SIGTERM=SIGQUIT celery worker --app girder.celery --schedule /tmp/celerybeat-schedule.db --pidfile /tmp/clerybeat.pid --loglevel info --without-heartbeat
