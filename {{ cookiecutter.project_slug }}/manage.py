#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line


def main() -> None:
    # Production usage runs manage.py for tasks like collectstatic,
    # so DJANGO_SETTINGS_MODULE should always be explicitly set in production
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.pkg_name }}.settings.development')

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
