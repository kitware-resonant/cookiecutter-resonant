"""
Configure Django Extensions.

This requires the `django-extensions` package to be installed.
"""

from __future__ import annotations

SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_PRINT_SQL_TRUNCATE = None
RUNSERVER_PLUS_PRINT_SQL_TRUNCATE = None

__all__ = [
    "RUNSERVER_PLUS_PRINT_SQL_TRUNCATE",
    "SHELL_PLUS_PRINT_SQL",
    "SHELL_PLUS_PRINT_SQL_TRUNCATE",
]
