from __future__ import annotations

from pathlib import Path

from composed_configuration import (
    ComposedConfiguration,
    ConfigMixin,
    DevelopmentBaseConfiguration,
    HerokuProductionBaseConfiguration,
    TestingBaseConfiguration,
)


class {{ cookiecutter.pkg_name.split('_')|map('capitalize')|join('') }}Mixin(ConfigMixin):
    WSGI_APPLICATION = '{{ cookiecutter.pkg_name }}.wsgi.application'
    ROOT_URLCONF = '{{ cookiecutter.pkg_name }}.urls'

    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

    @staticmethod
    def mutate_configuration(configuration: ComposedConfiguration) -> None:
        # Install local apps first, to ensure any overridden resources are found first
        configuration.INSTALLED_APPS = [
            '{{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.apps.{{ cookiecutter.first_app_name.split('_')|map('capitalize')|join('') }}Config',
        ] + configuration.INSTALLED_APPS

        # Install additional apps
        configuration.INSTALLED_APPS += [
            's3_file_field',
        ]


class DevelopmentConfiguration({{ cookiecutter.pkg_name.split('_')|map('capitalize')|join('') }}Mixin, DevelopmentBaseConfiguration):
    SHELL_PLUS_IMPORTS = [
        'from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }} import tasks',
    ]


class TestingConfiguration({{ cookiecutter.pkg_name.split('_')|map('capitalize')|join('') }}Mixin, TestingBaseConfiguration):
    pass


class HerokuProductionConfiguration({{ cookiecutter.pkg_name.split('_')|map('capitalize')|join('') }}Mixin, HerokuProductionBaseConfiguration):
    pass
