from ._base import ComposedConfiguration, ConfigMixin


class ExtensionsMixin(ConfigMixin):
    """
    Configure Django Extensions.

    This requires the `django-extensions` package to be installed.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        configuration.INSTALLED_APPS += ["django_extensions"]

    SHELL_PLUS_PRINT_SQL = True
    SHELL_PLUS_PRINT_SQL_TRUNCATE = None
    RUNSERVER_PLUS_PRINT_SQL_TRUNCATE = None
