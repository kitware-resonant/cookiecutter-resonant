from __future__ import annotations

from pathlib import Path

from django_girders.configuration import DevelopmentBaseConfiguration


class DevelopmentConfiguration(DevelopmentBaseConfiguration):
    WSGI_APPLICATION = '{{ cookiecutter.pkg_name }}.wsgi.application'
    ROOT_URLCONF = '{{ cookiecutter.pkg_name }}.urls'

    BASE_DIR = str(Path(__file__).absolute().parent.parent)

    @staticmethod
    def before_binding(configuration: DevelopmentConfiguration) -> None:
        configuration.INSTALLED_APPS += ['{{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.apps.{{ cookiecutter.first_app_name.capitalize() }}Config']
