from resonant_settings._env import env

# Acknowledge early in development, which will help prevent failing or
# long-running tasks from being started automatically every time the worker
# process restarts; this more aggressively flushes the task queue.
CELERY_TASK_ACKS_LATE = False

CELERY_TASK_ALWAYS_EAGER: bool = env.bool("DJANGO_CELERY_TASK_ALWAYS_EAGER", default=False)
CELERY_TASK_EAGER_PROPAGATES = CELERY_TASK_ALWAYS_EAGER

# In development, run without concurrency.
CELERY_WORKER_CONCURRENCY: int | None = 1
