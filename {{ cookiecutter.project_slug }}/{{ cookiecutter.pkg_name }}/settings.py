from __future__ import annotations

from pathlib import Path

from django_girders.configuration import (
    ComposedConfiguration,
    ConfigMixin,
    DevelopmentBaseConfiguration,
    HerokuProductionBaseConfiguration,
    ProductionBaseConfiguration,
    TestingBaseConfiguration,
)


class {{ cookiecutter.pkg_name.split('_')|map('capitalize')|join('') }}Config(ConfigMixin):
    WSGI_APPLICATION = '{{ cookiecutter.pkg_name }}.wsgi.application'
    ROOT_URLCONF = '{{ cookiecutter.pkg_name }}.urls'

    BASE_DIR = str(Path(__file__).absolute().parent.parent)

    @staticmethod
    def before_binding(configuration: ComposedConfiguration) -> None:
        configuration.INSTALLED_APPS += ['{{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.apps.{{ cookiecutter.first_app_name.split('_')|map('capitalize')|join('') }}Config']


class DevelopmentConfiguration({{ cookiecutter.pkg_name.split('_')|map('capitalize')|join('') }}Config, DevelopmentBaseConfiguration):
    pass


class TestingConfiguration({{ cookiecutter.pkg_name.split('_')|map('capitalize')|join('') }}Config, TestingBaseConfiguration):
    pass


class ProductionConfiguration({{ cookiecutter.pkg_name.split('_')|map('capitalize')|join('') }}Config, ProductionBaseConfiguration):
    pass


class HerokuProductionConfiguration({{ cookiecutter.pkg_name.split('_')|map('capitalize')|join('') }}Config, HerokuProductionBaseConfiguration):
    pass
