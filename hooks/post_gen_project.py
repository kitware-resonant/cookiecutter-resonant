#!/usr/bin/env python3

import os
import shutil


EXAMPLE_MODELS_REMOVE = [
    '{{ cookiecutter.project_slug }}/{{ cookiecutter.first_app_name }}/admin/image.py',
    '{{ cookiecutter.project_slug }}/{{ cookiecutter.first_app_name }}/migrations/0002_initial_models.py',
    '{{ cookiecutter.project_slug }}/{{ cookiecutter.first_app_name }}/models/image.py',
    '{{ cookiecutter.project_slug }}/{{ cookiecutter.first_app_name }}/rest/image.py',
    '{{ cookiecutter.project_slug }}/{{ cookiecutter.first_app_name }}/templates/gallery.html',
    '{{ cookiecutter.project_slug }}/{{ cookiecutter.first_app_name }}/templates/summary.html',
    '{{ cookiecutter.project_slug }}/{{ cookiecutter.first_app_name }}/tests/test_image.py'
]

def _delete_resource(resource):
    if os.path.isfile(resource):
        os.remove(resource)
    elif os.path.isdir(resource):
        shutil.rmtree(resource)

def example_models_hook():
    for path in EXAMPLE_MODELS_REMOVE:
        _delete_resource(path)

def run_hooks():
    if '{{ cookiecutter.example_models }}' != 'yes':
        example_models_hook()

if __name__ == "__main__":
    run_hooks()
