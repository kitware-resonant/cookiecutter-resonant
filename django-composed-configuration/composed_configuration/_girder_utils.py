from ._base import ComposedConfiguration, ConfigMixin


class GirderUtilsMixin(ConfigMixin):
    """
    Configure girder_utils template tags.

    This requires the `django-girder-utils` package to be installed.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        configuration.INSTALLED_APPS += ["girder_utils"]
