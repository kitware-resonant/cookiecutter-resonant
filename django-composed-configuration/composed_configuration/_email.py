from typing import cast

from configurations import values

from ._base import ComposedConfiguration, ConfigMixin


class _EmailMixin(ConfigMixin):
    """Abstract base for email configs."""

    pass


class SmtpEmailMixin(_EmailMixin):
    """
    Configure Django's email sending.

    The following environment variables must be externally set:
    * `DJANGO_EMAIL_URL`, as a URL for login to an STMP server, as parsed by `dj-email-url`. This
      typically will start with `submission:`. Special characters in passwords must be URL-encoded.
      See https://pypi.org/project/dj-email-url/ for full details.
    * `DJANGO_DEFAULT_FROM_EMAIL`, as the default From address for outgoing email.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        email = cast(
            dict[str, str],
            values.EmailURLValue(
                environ_name="EMAIL_URL",
                environ_prefix="DJANGO",
                environ_required=True,
                # Disable late_binding, to make this return a usable value (which is a simple dict)
                # immediately
                late_binding=False,
            ),
        )
        for email_setting, email_setting_value in email.items():
            setattr(configuration, email_setting, email_setting_value)

    # Set both settings from DJANGO_DEFAULT_FROM_EMAIL
    DEFAULT_FROM_EMAIL = values.EmailValue(environ_required=True)
    SERVER_EMAIL = values.EmailValue(environ_name="DEFAULT_FROM_EMAIL", environ_required=True)


class ConsoleEmailMixin(_EmailMixin):
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
