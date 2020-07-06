from django.apps import AppConfig


class {{ cookiecutter.first_app_name.split('_')|map('capitalize')|join('') }}Config(AppConfig):
    name = '{{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}'
    verbose_name = '{{ cookiecutter.project_name }}: {{ cookiecutter.first_app_name.split('_')|map('capitalize')|join(' ') }}'
