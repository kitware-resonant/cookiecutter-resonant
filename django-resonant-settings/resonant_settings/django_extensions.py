"""
Configure Django Extensions.

This requires the `django-extensions` package to be installed.
"""

SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_PRINT_SQL_TRUNCATE = None
RUNSERVER_PLUS_PRINT_SQL_TRUNCATE = None

__all__ = [
    "SHELL_PLUS_PRINT_SQL",
    "SHELL_PLUS_PRINT_SQL_TRUNCATE",
    "RUNSERVER_PLUS_PRINT_SQL_TRUNCATE",
]
