from configurations import values

from ._allauth import AllauthMixin
from ._base import ComposedConfiguration
from ._celery import CeleryMixin
from ._cors import CorsMixin
from ._database import DatabaseMixin
from ._debug import DebugMixin
from ._django import DjangoMixin
from ._docker import _AlwaysContains, _is_docker
from ._email import ConsoleEmailMixin, SmtpEmailMixin
from ._extensions import ExtensionsMixin
from ._filter import FilterMixin
from ._girder_utils import GirderUtilsMixin
from ._https import HttpsMixin
from ._logging import LoggingMixin
from ._rest_framework import RestFrameworkMixin
from ._sentry import SentryMixin
from ._static import WhitenoiseStaticFileMixin
from ._storage import MinioStorageMixin, S3StorageMixin


# Subclasses are loaded in last to first ordering
class _BaseConfiguration(
    GirderUtilsMixin,
    ExtensionsMixin,
    CeleryMixin,
    RestFrameworkMixin,
    FilterMixin,
    # CorsMixin must be loaded after WhitenoiseStaticFileMixin
    CorsMixin,
    WhitenoiseStaticFileMixin,
    DatabaseMixin,
    LoggingMixin,
    AllauthMixin,
    # DjangoMixin should be loaded first
    DjangoMixin,
    ComposedConfiguration,
):
    pass


class DevelopmentBaseConfiguration(
    DebugMixin, ConsoleEmailMixin, MinioStorageMixin, _BaseConfiguration
):
    DEBUG = True
    SECRET_KEY = "insecuresecret"

    ALLOWED_HOSTS = values.ListValue(["localhost", "127.0.0.1"])
    CORS_ORIGIN_REGEX_WHITELIST = values.ListValue(
        [r"^https?://localhost:\d+$", r"^https?://127\.0\.0\.1:\d+$"]
    )

    # When in Docker, the bridge network sends requests from the host machine exclusively via a
    # dedicated IP address. Since there's no way to determine the real origin address,
    # consider any IP address (though actually this will only be the single dedicated address) to
    # be internal. This relies on the host to set up appropriate firewalls for Docker, to prevent
    # access from non-internal addresses.
    INTERNAL_IPS = _AlwaysContains() if _is_docker() else ["127.0.0.1"]
    # Setting this allows MinIO to work through network namespace partitions
    # (e.g. when running within Docker Compose)
    MINIO_STORAGE_MEDIA_URL = values.Value(None)


class TestingBaseConfiguration(MinioStorageMixin, _BaseConfiguration):
    SECRET_KEY = "testingsecret"

    # Testing will add 'testserver' to ALLOWED_HOSTS
    ALLOWED_HOSTS: list[str] = []

    MINIO_STORAGE_MEDIA_BUCKET_NAME = "test-django-storage"

    # Testing will set EMAIL_BACKEND to use the memory backend


class ProductionBaseConfiguration(
    SentryMixin, SmtpEmailMixin, S3StorageMixin, HttpsMixin, _BaseConfiguration
):
    pass


# Separate these settings for potential reuse, but this may not be usable enough to make public
# yet, given the fragility of ensuring that this is added as a superclass in the correct order.
class _HerokuMixin:
    # Use different env var names (with no DJANGO_ prefix) for services that Heroku auto-injects
    DATABASES = values.DatabaseURLValue(
        environ_name="DATABASE_URL",
        environ_prefix=None,
        environ_required=True,
        engine="django.db.backends.postgresql",
        conn_max_age=600,
        ssl_require=True,
    )
    CELERY_BROKER_URL = values.Value(
        environ_name="CLOUDAMQP_URL", environ_prefix=None, environ_required=True
    )
    # https://help.heroku.com/J2R1S4T8/can-heroku-force-an-application-to-use-ssl-tls
    SECURE_PROXY_SSL_HEADER: tuple[str, str] | None = ("HTTP_X_FORWARDED_PROTO", "https")
    # This may be provided by https://github.com/ianpurvis/heroku-buildpack-version or similar
    # The commit SHA is the preferred release tag for Git-based projects:
    # https://docs.sentry.io/platforms/python/configuration/releases/#bind-the-version
    SENTRY_RELEASE = values.Value(
        None,
        environ_name="SOURCE_VERSION",
        environ_prefix=None,
    )


class HerokuProductionBaseConfiguration(_HerokuMixin, ProductionBaseConfiguration):
    pass
