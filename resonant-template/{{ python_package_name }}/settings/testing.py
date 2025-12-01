from secrets import randbelow

from .base import *

# Import these afterwards, to override
from resonant_settings.development.minio_storage import *  # isort: skip

SECRET_KEY = 'insecure-secret'

# Use a fast, insecure hasher to speed up tests
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']

STORAGES['default'] = {
    'BACKEND': 'minio_storage.storage.MinioMediaStorage',
}
MINIO_STORAGE_MEDIA_BUCKET_NAME = f'test-django-storage-{randbelow(1_000_000):06d}'

# Testing will set EMAIL_BACKEND to use the memory backend
