from django.apps import AppConfig


class {{ cookiecutter.first_app_name.capitalize() }}Config(AppConfig):
    name = '{{ cookiecutter.first_app_name }}'
