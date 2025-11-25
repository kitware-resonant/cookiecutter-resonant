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
# it isn't the upstream default only for backwards compatibility reasons.
AWS_S3_SIGNATURE_VERSION = "s3v4"

AWS_S3_MAX_MEMORY_SIZE = 5 * 1024 * 1024

# Although overwriting existing files can be dangerous, it's the application's responsibility
# (not the Storage layer) to handle. Setting this to `False` allows file names to be mutated in
# the event of a collision, which can be confusing.
AWS_S3_FILE_OVERWRITE = True
AWS_QUERYSTRING_EXPIRE = int(timedelta(hours=6).total_seconds())

__all__ = [
    "AWS_S3_REGION_NAME",
    "AWS_S3_ACCESS_KEY_ID",
    "AWS_S3_SECRET_ACCESS_KEY",
    "AWS_STORAGE_BUCKET_NAME",
    "AWS_S3_SIGNATURE_VERSION",
    "AWS_S3_MAX_MEMORY_SIZE",
    "AWS_S3_FILE_OVERWRITE",
    "AWS_QUERYSTRING_EXPIRE",
]
