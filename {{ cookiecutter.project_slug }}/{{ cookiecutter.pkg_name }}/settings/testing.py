from .base import *

SECRET_KEY = 'insecure-secret'

# Use a fast, insecure hasher to speed up tests, but keep existing hashers for development use
# when reading a production databases.
PASSWORD_HASHERS.insert(0, 'django.contrib.auth.hashers.MD5PasswordHasher')

STORAGES['default'] = {
    'BACKEND': 'minio_storage.storage.MinioMediaStorage',
}
from resonant_settings.testing.minio_storage import *  # isort: skip

# Testing will set EMAIL_BACKEND to use the memory backend

MINIO_STORAGE_MEDIA_BUCKET_NAME = 'test-django-storage'
