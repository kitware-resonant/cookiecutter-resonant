#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys

EXAMPLE_CODE_REMOVE = [
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/admin/image.py',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/migrations/0002_initial_models.py',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/models/image.py',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/rest/image.py',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/templates/{{ cookiecutter.first_app_name }}/gallery.html',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/templates/{{ cookiecutter.first_app_name }}/summary.html',
    '{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/tests/test_image.py',
]


def _delete_resource(resource):
    if os.path.isfile(resource):
        os.remove(resource)
        return True
    elif os.path.isdir(resource):
        shutil.rmtree(resource)
        return True
    return False


def include_example_code_hook():
    for path in EXAMPLE_CODE_REMOVE:
        resource = os.path.join(os.getcwd(), path)
        if _delete_resource(resource):
            print(f'Removed resource {resource}')
        else:
            print(f'Failed to remove {resource}')
            sys.exit(1)


def uv_lock_hook():
    subprocess.check_call(['uv', 'lock'])


def run_hooks():
    if '{{ cookiecutter.include_example_code }}' != 'yes':
        include_example_code_hook()
    uv_lock_hook()


if __name__ == "__main__":
    run_hooks()
