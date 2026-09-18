from __future__ import annotations

from secrets import randbelow

from .base import *

# Import these afterwards, to override
from resonant_settings.development.minio_storage import *

SECRET_KEY = "insecure-secret"

# Use a fast, insecure hasher to speed up tests
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

STORAGES["default"] = {
    "BACKEND": "minio_storage.storage.MinioMediaStorage",
}
MINIO_STORAGE_MEDIA_BUCKET_NAME = f"test-django-storage-{randbelow(1_000_000):06d}"

# Django's test runner will override every mailer here with the memory backend, but a "default"
# mailer must exist for outgoing email to be captured instead of failing.
MAILERS: dict[str, dict[str, Any]] = {
    "default": {
        "BACKEND": "django.core.mail.backends.locmem.EmailBackend",
    },
}
