from ._base import ComposedConfiguration, ConfigMixin


class DebugMixin(ConfigMixin):
    """
    Configure debug tooling.

    This requires the `django-debug-toolbar` package to be installed.
    """

    @staticmethod
    def mutate_configuration(configuration: type[ComposedConfiguration]) -> None:
        configuration.INSTALLED_APPS += ["debug_toolbar"]

        # Include Debug Toolbar middleware as early as possible in the list.
        # However, it must come after any other middleware that encodes the response’s content,
        # such as GZipMiddleware.
        configuration.MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

    DEBUG_TOOLBAR_CONFIG = {
        # The default size often is too small, causing an inability to view queries
        "RESULTS_CACHE_SIZE": 250,
        # If this setting is True, large sql queries can cause the page to render slowly
        "PRETTIFY_SQL": False,
    }
