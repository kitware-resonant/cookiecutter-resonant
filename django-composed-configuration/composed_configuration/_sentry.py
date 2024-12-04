from configurations import values

from ._base import ComposedConfiguration, ConfigMixin


class SentryMixin(ConfigMixin):
    """
    Configure Sentry.io error reporting.

    This requires the `sentry-sdk` package to be installed.

    The `DJANGO_SENTRY_DSN` environment variable should be externally set to a Sentry DSN.

    The `DJANGO_SENTRY_ENVIRONMENT`, `DJANGO_SENTRY_RELEASE`, `DJANGO_SENTRY_TRACES_SAMPLE_RATE`,
    and `DJANGO_SENTRY_PROFILES_SAMPLE_RATE` environment variables may also be set, if desired.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        configuration.INSTALLED_APPS += [
            "composed_configuration.sentry.apps.SentryConfig",
        ]

    SENTRY_DSN = values.Value(None)

    SENTRY_ENVIRONMENT = values.Value(None)

    SENTRY_RELEASE = values.Value(None)

    # None is a valid default value for these rates, but if set via environment variable,
    # the values must be interpretable as floats
    SENTRY_TRACES_SAMPLE_RATE = values.FloatValue(None)
    SENTRY_PROFILES_SAMPLE_RATE = values.FloatValue(None)
