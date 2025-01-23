# Acknowledge early in development, which will help prevent failing or
# long-running tasks from being started automatically every time the worker
# process restarts; this more aggressively flushes the task queue.
CELERY_TASK_ACKS_LATE = False

# In development, run without concurrency.
CELERY_WORKER_CONCURRENCY: int | None = 1
