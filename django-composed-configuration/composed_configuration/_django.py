from typing import NoReturn

from configurations import values

from ._base import ComposedConfiguration, ConfigMixin


class DjangoMixin(ConfigMixin):
    """
    Configure a basic Django project.

    Downstreams must explicitly define the settings:
    * `WSGI_APPLICATION`, as a string with the Python import path of the WSGI `application` in the
      `wsgi.py` file.
    * `ROOT_URLCONF`, as a string with the Python import path of the base `urls.py` file.

    The following environment variables must be externally set:
    * `SECRET_KEY`, as a random string.
    * `DJANGO_ALLOWED_HOSTS`, as a comma-delimited list of fully-qualified domain names from
       which this server will be accessed.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        # These are often extended, so update their values to avoid fragility due to mixin ordering
        configuration.INSTALLED_APPS += [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.humanize",
        ]
        configuration.MIDDLEWARE += [
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ]

    SECRET_KEY = values.SecretValue()
    ALLOWED_HOSTS = values.ListValue(environ_required=True)

    @property
    def WSGI_APPLICATION(self) -> NoReturn:  # noqa: N802
        raise Exception("WSGI_APPLICATION must be explicitly set.")

    @property
    def ROOT_URLCONF(self) -> NoReturn:  # noqa: N802
        raise Exception("ROOT_URLCONF must be explicitly set.")

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    PASSWORD_HASHERS = [
        # Argon2 is recommended by OWASP, so make it the default for new passwords
        # https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
        "django.contrib.auth.hashers.Argon2PasswordHasher",
        # scrypt was the default hasher in older versions of composed-configuration,
        # so it must be enabled to read old passwords
        "django.contrib.auth.hashers.ScryptPasswordHasher",
        # Support for other hashers isn't needed,
        # since databases shouldn't have entries with other algorithms
    ]
    # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/
    LANGUAGE_CODE = "en-us"
    USE_TZ = True
    TIME_ZONE = "UTC"
    USE_I18N = True
