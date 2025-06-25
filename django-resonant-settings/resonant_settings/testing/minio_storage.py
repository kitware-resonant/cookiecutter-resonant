"""
Configure MinioMediaStorage.

This requires the `django-minio-storage` package to be installed.
"""

from urllib.parse import ParseResult

from resonant_settings._env import env

minio_url: ParseResult = env.url("DJANGO_MINIO_STORAGE_URL")
MINIO_STORAGE_USE_HTTPS = minio_url.scheme == "https"
MINIO_STORAGE_ENDPOINT = (
    f"{minio_url.hostname}:{minio_url.port}" if minio_url.port else minio_url.hostname
)
MINIO_STORAGE_ACCESS_KEY = minio_url.username
MINIO_STORAGE_SECRET_KEY = minio_url.password
MINIO_STORAGE_MEDIA_BUCKET_NAME = minio_url.path.lstrip("/")

# Setting this allows MinIO to work through network namespace partitions
# (e.g. when running within Docker Compose)
MINIO_STORAGE_MEDIA_URL: str | None = env.str("DJANGO_MINIO_STORAGE_MEDIA_URL", default=None)

MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
# Make the bucket private to the public
MINIO_STORAGE_AUTO_CREATE_MEDIA_POLICY = "NONE"
# Issue signed URLs to provide any read access
MINIO_STORAGE_MEDIA_USE_PRESIGNED = True
