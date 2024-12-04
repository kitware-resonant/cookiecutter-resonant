from configurations import values

from ._base import ComposedConfiguration, ConfigMixin


class _StorageMixin(ConfigMixin):
    """Abstract base for storage configs."""

    pass
    # For unity, subclasses should use "environ_name='STORAGE_BUCKET_NAME'" for
    # whatever particular setting is used to store the bucket name


class MinioStorageMixin(_StorageMixin):
    """
    Configure MinioMediaStorage.

    The following environment variables must be externally set:
    * DJANGO_MINIO_STORAGE_ACCESS_KEY
    * DJANGO_MINIO_STORAGE_SECRET_KEY
    * DJANGO_STORAGE_BUCKET_NAME

    This requires the `django-minio-storage` package to be installed.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        configuration.STORAGES.update(
            {
                "default": {
                    "BACKEND": "minio_storage.storage.MinioMediaStorage",
                }
            }
        )

    MINIO_STORAGE_ENDPOINT = values.Value("localhost:9000")
    MINIO_STORAGE_USE_HTTPS = values.BooleanValue(False)
    MINIO_STORAGE_ACCESS_KEY = values.SecretValue()
    MINIO_STORAGE_SECRET_KEY = values.SecretValue()
    MINIO_STORAGE_MEDIA_BUCKET_NAME = values.Value(
        environ_name="STORAGE_BUCKET_NAME", environ_required=True
    )
    MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
    MINIO_STORAGE_AUTO_CREATE_MEDIA_POLICY = "READ_WRITE"
    MINIO_STORAGE_MEDIA_USE_PRESIGNED = True


class S3StorageMixin(_StorageMixin):
    """
    Configure S3Boto3Storage.

    The following environment variables must be externally set:
    * AWS_DEFAULT_REGION
    * AWS_ACCESS_KEY_ID
    * AWS_SECRET_ACCESS_KEY
    * DJANGO_STORAGE_BUCKET_NAME

    This requires the `django-storages[boto3]` package to be installed.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        configuration.STORAGES.update(
            {
                "default": {
                    "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
                }
            }
        )

    # This exact environ_name is important, as direct use of Boto will also use it
    AWS_S3_REGION_NAME = values.Value(
        environ_prefix=None, environ_name="AWS_DEFAULT_REGION", environ_required=True
    )
    AWS_S3_ACCESS_KEY_ID = values.Value(
        environ_prefix=None, environ_name="AWS_ACCESS_KEY_ID", environ_required=True
    )
    AWS_S3_SECRET_ACCESS_KEY = values.Value(
        environ_prefix=None, environ_name="AWS_SECRET_ACCESS_KEY", environ_required=True
    )

    AWS_STORAGE_BUCKET_NAME = values.Value(
        environ_name="STORAGE_BUCKET_NAME", environ_required=True
    )

    # It's critical to use the v4 signature;
    # it isn't the upstream default only for backwards compatability reasons.
    AWS_S3_SIGNATURE_VERSION = "s3v4"

    AWS_S3_MAX_MEMORY_SIZE = 5 * 1024 * 1024
    AWS_S3_FILE_OVERWRITE = False
    AWS_QUERYSTRING_EXPIRE = 3600 * 6  # 6 hours
