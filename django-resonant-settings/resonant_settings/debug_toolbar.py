"""
Configure Django Debug Toolbar with the following features:
* Improve performance with large queries

This requires the `django-debug-toolbar` package to be installed.
"""

DEBUG_TOOLBAR_CONFIG = {
    # The default size often is too small, causing an inability to view queries
    "RESULTS_CACHE_SIZE": 250,
    # If this setting is True, large sql queries can cause the page to render slowly
    "PRETTIFY_SQL": False,
}
