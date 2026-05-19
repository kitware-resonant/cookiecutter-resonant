from __future__ import annotations

from resonant_settings._env import env

# Acknowledge early in development, which will help prevent failing or
# long-running tasks from being started automatically every time the worker
# process restarts; this more aggressively flushes the task queue.
CELERY_TASK_ACKS_LATE = False

CELERY_TASK_ALWAYS_EAGER: bool = env.bool("DJANGO_CELERY_TASK_ALWAYS_EAGER", default=False)
# In eager mode (which might be set directly in tests), non-propagated exceptions allow bugs to go
# unnoticed, so ensure this is always enabled. This should have no effect in non-eager mode.
CELERY_TASK_EAGER_PROPAGATES = True

# Run without concurrency, in the main process, to ease debugging.
CELERY_WORKER_POOL = "solo"
CELERY_WORKER_CONCURRENCY: int | None = 1

# Fail faster to improve developer ergonomics.
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = False
CELERY_BROKER_CONNECTION_TIMEOUT: float | None = 5

__all__ = [
    "CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP",
    "CELERY_BROKER_CONNECTION_TIMEOUT",
    "CELERY_TASK_ACKS_LATE",
    "CELERY_TASK_ALWAYS_EAGER",
    "CELERY_TASK_EAGER_PROPAGATES",
    "CELERY_WORKER_CONCURRENCY",
    "CELERY_WORKER_POOL",
]
