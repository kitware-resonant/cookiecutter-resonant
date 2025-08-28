"""
Configure S3Storage.

The following environment variables must be externally set:
* AWS_DEFAULT_REGION
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* DJANGO_STORAGE_BUCKET_NAME

This requires the `django-storages[s3]` package to be installed.
"""

from datetime import timedelta

from resonant_settings._env import env

# These exact environment variable names are important,
# as direct instantiations of Boto will also respect them.
AWS_S3_REGION_NAME: str = env.str("AWS_DEFAULT_REGION")
AWS_S3_ACCESS_KEY_ID: str = env.str("AWS_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY: str = env.str("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME: str = env.str("DJANGO_STORAGE_BUCKET_NAME")

# It's critical to use the v4 signature;
# it isn't the upstream default only for backwards compatability reasons.
AWS_S3_SIGNATURE_VERSION = "s3v4"

AWS_S3_MAX_MEMORY_SIZE = 5 * 1024 * 1024
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_EXPIRE = int(timedelta(hours=6).total_seconds())
