from configurations import values

from ._base import ComposedConfiguration, ConfigMixin


class CorsMixin(ConfigMixin):
    """
    Configure CORS headers.

    The following environment variables may be externally set:
    * `DJANGO_CORS_ORIGIN_WHITELIST`
    * `DJANGO_CORS_ORIGIN_REGEX_WHITELIST`

    This requires the `django-cors-headers` package to be installed.
    This also must be loaded after `WhitenoiseStaticFileMixin`.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        configuration.INSTALLED_APPS += ["corsheaders"]

        # CorsMiddleware must be added immediately before WhiteNoiseMiddleware, so this can
        # potentially add CORS headers to those responses too.
        # Accordingly, CorsMixin must be loaded after WhitenoiseStaticFileMixin, so it can
        # find the existing entry and insert accordingly.
        try:
            whitenoise_index = configuration.MIDDLEWARE.index(
                "whitenoise.middleware.WhiteNoiseMiddleware"
            )
        except ValueError:
            raise Exception("CorsConfig must be loaded after WhitenoiseStaticFileMixin.")
        configuration.MIDDLEWARE.insert(whitenoise_index, "corsheaders.middleware.CorsMiddleware")

    CORS_ORIGIN_WHITELIST = values.ListValue()
    CORS_ORIGIN_REGEX_WHITELIST = values.ListValue()
