from ._base import ComposedConfiguration, ConfigMixin


class AllauthMixin(ConfigMixin):
    """
    Configure Django Allauth.

    This requires the django-allauth package to be installed.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        configuration.INSTALLED_APPS += [
            "django.contrib.sites",
            "allauth",
            "allauth.account",
            "allauth.socialaccount",
        ]

        # Insert before before auth, so the overridden createsuperuser command is found first
        auth_index = configuration.INSTALLED_APPS.index("django.contrib.auth")
        configuration.INSTALLED_APPS.insert(
            auth_index, "composed_configuration._allauth_support.apps.AllauthSupportConfig"
        )

        # auth_style should come before others, to ensure its template overrides are found
        configuration.INSTALLED_APPS.insert(0, "auth_style")

        configuration.MIDDLEWARE += [
            "allauth.account.middleware.AccountMiddleware",
        ]

    # The sites framework requires this to be set.
    # In the unlikely case where a database's pk sequence for the django_site table is not reset,
    # the default site object could have a different pk. Then this will need to be overridden
    # downstream.
    SITE_ID = 1

    AUTHENTICATION_BACKENDS = [
        # Django's built-in ModelBackend is not necessary, since all users will be
        # authenticated by their email address
        "allauth.account.auth_backends.AuthenticationBackend",
    ]

    # see configuration documentation at
    #   https://django-allauth.readthedocs.io/en/latest/configuration.html

    # Require email verification, but this can be overridden
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"

    # Make Django and Allauth redirects consistent, but both may be overridden
    LOGIN_REDIRECT_URL = "/"
    ACCOUNT_LOGOUT_REDIRECT_URL = "/"

    # Use email as the identifier for login
    ACCOUNT_AUTHENTICATION_METHOD = "email"
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False

    # Set the username as the email
    ACCOUNT_ADAPTER = (
        "composed_configuration._allauth_support.adapter.EmailAsUsernameAccountAdapter"
    )
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None

    # Quality of life improvements, but may not work if the browser is closed
    ACCOUNT_SESSION_REMEMBER = True
    ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
    ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

    # These will permit GET requests to mutate the user state, but significantly improve usability
    ACCOUNT_LOGOUT_ON_GET = True
    ACCOUNT_CONFIRM_EMAIL_ON_GET = True

    # This will likely become the default in the future, but enable it now
    ACCOUNT_PRESERVE_USERNAME_CASING = False
