"""
Configure MinioMediaStorage.

This requires the `django-minio-storage` package to be installed.
The storage server itself is SeaweedFS, which is S3-compatible.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from resonant_settings._env import env

if TYPE_CHECKING:
    from urllib.parse import ParseResult

minio_url: ParseResult = env.url("DJANGO_MINIO_STORAGE_URL")
MINIO_STORAGE_USE_HTTPS = minio_url.scheme == "https"
MINIO_STORAGE_ENDPOINT = (
    f"{minio_url.hostname}:{minio_url.port}" if minio_url.port else minio_url.hostname
)
MINIO_STORAGE_ACCESS_KEY = minio_url.username
MINIO_STORAGE_SECRET_KEY = minio_url.password
MINIO_STORAGE_MEDIA_BUCKET_NAME = minio_url.path.lstrip("/")

# Setting this allows the storage server to work through network namespace partitions
# (e.g. when running within Docker Compose)
MINIO_STORAGE_MEDIA_URL: str | None = env.str("DJANGO_MINIO_STORAGE_MEDIA_URL", default=None)

MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
# New buckets are already private to the public, so don't set any policy on them.
# A "NONE" policy would send an empty policy document, which SeaweedFS rejects.
MINIO_STORAGE_AUTO_CREATE_MEDIA_POLICY = False
# Issue signed URLs to provide any read access
MINIO_STORAGE_MEDIA_USE_PRESIGNED = True

__all__ = [
    "MINIO_STORAGE_ACCESS_KEY",
    "MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET",
    "MINIO_STORAGE_AUTO_CREATE_MEDIA_POLICY",
    "MINIO_STORAGE_ENDPOINT",
    "MINIO_STORAGE_MEDIA_BUCKET_NAME",
    "MINIO_STORAGE_MEDIA_URL",
    "MINIO_STORAGE_MEDIA_USE_PRESIGNED",
    "MINIO_STORAGE_SECRET_KEY",
    "MINIO_STORAGE_USE_HTTPS",
]
