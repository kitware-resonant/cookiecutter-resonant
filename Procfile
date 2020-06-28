release: ./manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT {{ pkg_name }}.wsgi
worker: REMAP_SIGTERM=SIGQUIT celery worker --app {{ pkg_name }}.celery --loglevel info --without-heartbeat
