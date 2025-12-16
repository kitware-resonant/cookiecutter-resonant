from resonant_settings._env import env

# Acknowledge early in development, which will help prevent failing or
# long-running tasks from being started automatically every time the worker
# process restarts; this more aggressively flushes the task queue.
CELERY_TASK_ACKS_LATE = False

CELERY_TASK_ALWAYS_EAGER: bool = env.bool("DJANGO_CELERY_TASK_ALWAYS_EAGER", default=False)
# In eager mode (which might be set directly in tests), non-propagated exceptions allow bugs to go
# unnoticed, so ensure this is always enabled. This should have no effect in non-eager mode.
CELERY_TASK_EAGER_PROPAGATES = True

# In development, run without concurrency.
CELERY_WORKER_CONCURRENCY: int | None = 1

__all__ = [
    "CELERY_TASK_ACKS_LATE",
    "CELERY_TASK_ALWAYS_EAGER",
    "CELERY_TASK_EAGER_PROPAGATES",
    "CELERY_WORKER_CONCURRENCY",
]
