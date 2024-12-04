import logging

from django.apps import AppConfig
from django.conf import settings
import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


class SentryConfig(AppConfig):
    name = "composed_configuration.sentry"
    verbose_name = "Composed configuration Sentry support"

    def ready(self):
        sentry_sdk.init(
            # If a "dsn" is not explicitly passed, sentry_sdk will attempt to find the DSN in
            # the SENTRY_DSN environment variable; however, by pulling it from an explicit setting,
            # it can be overridden by downstream project settings.
            dsn=settings.SENTRY_DSN,
            environment=settings.SENTRY_ENVIRONMENT,
            release=settings.SENTRY_RELEASE,
            integrations=[
                LoggingIntegration(level=logging.INFO, event_level=logging.WARNING),
                DjangoIntegration(),
                CeleryIntegration(),
            ],
            # Send traces for non-exception events too
            attach_stacktrace=True,
            # Submit request User info from Django
            send_default_pii=True,
            # These are None by default, so performance monitoring/profiling is opt-in
            traces_sample_rate=settings.SENTRY_TRACES_SAMPLE_RATE,
            profiles_sample_rate=settings.SENTRY_PROFILES_SAMPLE_RATE,
        )
