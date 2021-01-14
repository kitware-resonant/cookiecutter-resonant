#!/usr/bin/env python3

import os
import shutil
import sys

EXAMPLE_MODELS_REMOVE = [
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/admin/image.py',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/migrations/0002_initial_models.py',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/models/image.py',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/rest/image.py',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/templates/gallery.html',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/templates/summary.html',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/tests/test_image.py'
]

def _delete_resource(resource):
    if os.path.isfile(resource):
        os.remove(resource)
        return True
    elif os.path.isdir(resource):
        shutil.rmtree(resource)
        return True
    return False

def example_models_hook():
    for path in EXAMPLE_MODELS_REMOVE:
        resource = os.path.join(os.getcwd(), path)
        if _delete_resource(resource):
            print("Removed resource {}".format(resource))
        else:
            print("Failed to remove {}".format(resource))
            sys.exit(1)

def run_hooks():
    if '{{ cookiecutter.example_models }}' != 'yes':
        example_models_hook()

if __name__ == "__main__":
    run_hooks()
