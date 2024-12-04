from configurations import values

from ._base import ComposedConfiguration, ConfigMixin


class DatabaseMixin(ConfigMixin):
    """
    Configure a single PostgreSQL database.

    The `DJANGO_DATABASE_URL` environment variable must be externally set
    to a PostgreSQL URL including credentials and the database name.

    This requires the `psycopg` package to be installed.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        configuration.INSTALLED_APPS += ["django.contrib.postgres"]

    # This cannot have a default value, since the password and database
    # name are always set by the service admin.
    DATABASES = values.DatabaseURLValue(
        environ_name="DATABASE_URL",
        # django-configurations has environ_prefix=None by default here
        environ_prefix="DJANGO",
        environ_required=True,
        # Additional kwargs to DatabaseURLValue are passed to dj-database-url,
        # then passed through to the Django database options.
        engine="django.db.backends.postgresql",
        conn_max_age=600,
    )


class HerokuDatabaseMixin(DatabaseMixin):
    """
    Configure a single Heroku PostgreSQL database.

    The `DATABASE_URL` environment variable must be externally set
    to a PostgreSQL URL including credentials and the database name.
    """

    # Heroku sets the environment variable as DATABASE_URL, so drop the
    # DJANGO_ prefix.
    DATABASES = values.DatabaseURLValue(
        environ_name="DATABASE_URL",
        environ_prefix=None,
        environ_required=True,
        # Additional kwargs here.
        engine="django.db.backends.postgresql",
        conn_max_age=600,
        # Heroku is expected to always provide SSL.
        ssl_require=True,
    )
