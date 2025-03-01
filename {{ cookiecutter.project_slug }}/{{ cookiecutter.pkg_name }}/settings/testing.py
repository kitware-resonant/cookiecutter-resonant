from .base import *

SECRET_KEY = 'insecure-secret'

# Use a fast, insecure hasher to speed up tests
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']

STORAGES['default'] = {
    'BACKEND': 'minio_storage.storage.MinioMediaStorage',
}
from resonant_settings.testing.minio_storage import *  # isort: skip

# Testing will set EMAIL_BACKEND to use the memory backend

MINIO_STORAGE_MEDIA_BUCKET_NAME = 'test-django-storage'
