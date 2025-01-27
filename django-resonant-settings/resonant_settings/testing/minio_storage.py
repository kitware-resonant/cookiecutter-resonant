"""
Configure MinioMediaStorage.

The following environment variables must be externally set:
* DJANGO_MINIO_STORAGE_ENDPOINT
* DJANGO_MINIO_STORAGE_ACCESS_KEY
* DJANGO_MINIO_STORAGE_SECRET_KEY
* DJANGO_STORAGE_BUCKET_NAME

This requires the `django-minio-storage` package to be installed.
"""

from resonant_settings._env import env

MINIO_STORAGE_ENDPOINT: str = env.str("DJANGO_MINIO_STORAGE_ENDPOINT")
MINIO_STORAGE_USE_HTTPS: bool = env.bool("DJANGO_MINIO_STORAGE_USE_HTTPS", default=False)
MINIO_STORAGE_ACCESS_KEY: str = env.str("DJANGO_MINIO_STORAGE_ACCESS_KEY")
MINIO_STORAGE_SECRET_KEY: str = env.str("DJANGO_MINIO_STORAGE_SECRET_KEY")
# Use this name for unity with the S3 configuration
MINIO_STORAGE_MEDIA_BUCKET_NAME: str = env.str("DJANGO_STORAGE_BUCKET_NAME")
# Setting this allows MinIO to work through network namespace partitions
# (e.g. when running within Docker Compose)
MINIO_STORAGE_MEDIA_URL: str | None = env.str("DJANGO_MINIO_STORAGE_MEDIA_URL", default=None)
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_AUTO_CREATE_MEDIA_POLICY = "READ_WRITE"
MINIO_STORAGE_MEDIA_USE_PRESIGNED = True
