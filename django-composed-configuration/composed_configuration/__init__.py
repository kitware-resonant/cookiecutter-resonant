from importlib.metadata import PackageNotFoundError, version

from ._allauth import AllauthMixin
from ._base import ComposedConfiguration, ConfigMixin
from ._celery import CeleryMixin
from ._configuration import (
    DevelopmentBaseConfiguration,
    HerokuProductionBaseConfiguration,
    ProductionBaseConfiguration,
    TestingBaseConfiguration,
)
from ._cors import CorsMixin
from ._database import DatabaseMixin
from ._debug import DebugMixin
from ._django import DjangoMixin
from ._email import ConsoleEmailMixin, SmtpEmailMixin
from ._extensions import ExtensionsMixin
from ._filter import FilterMixin
from ._girder_utils import GirderUtilsMixin
from ._https import HttpsMixin
from ._logging import LoggingMixin
from ._rest_framework import RestFrameworkMixin
from ._sentry import SentryMixin
from ._static import StaticFileMixin, WhitenoiseStaticFileMixin
from ._storage import MinioStorageMixin, S3StorageMixin

__all__ = [
    "AllauthMixin",
    "CeleryMixin",
    "ComposedConfiguration",
    "ConfigMixin",
    "ConsoleEmailMixin",
    "CorsMixin",
    "DatabaseMixin",
    "DebugMixin",
    "DevelopmentBaseConfiguration",
    "DjangoMixin",
    "ExtensionsMixin",
    "FilterMixin",
    "GirderUtilsMixin",
    "HerokuProductionBaseConfiguration",
    "HttpsMixin",
    "LoggingMixin",
    "MinioStorageMixin",
    "ProductionBaseConfiguration",
    "RestFrameworkMixin",
    "S3StorageMixin",
    "SentryMixin",
    "SmtpEmailMixin",
    "StaticFileMixin",
    "TestingBaseConfiguration",
    "WhitenoiseStaticFileMixin",
]

try:
    __version__ = version("django-composed-configuration")
except PackageNotFoundError:
    # package is not installed
    pass
