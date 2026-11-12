from __future__ import annotations

from celery import Celery
from celery.contrib.django.task import DjangoTask

# Celery will automatically use DjangoTask, which we annotate to have any parameters and
# return None (since we don't use a results backend).
# Using a string config_source means the worker doesn't have to serialize
# the configuration object to child processes.
app = Celery[DjangoTask[..., None]](config_source="django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
