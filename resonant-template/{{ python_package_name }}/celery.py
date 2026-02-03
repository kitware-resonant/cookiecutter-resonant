from __future__ import annotations

from celery import Celery

# Using a string config_source means the worker doesn't have to serialize
# the configuration object to child processes.
app = Celery(config_source='django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
