#!/usr/bin/env python
import os
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
FIRST_APP_PATH = Path('{{ cookiecutter.pkg_name }}', '{{ cookiecutter.first_app_name }}')

SAMPLE_MODEL_FILES = [
    FIRST_APP_PATH / Path('admin', 'image.py'),
    FIRST_APP_PATH / Path('models', 'image.py'),
    FIRST_APP_PATH / Path('rest', 'image.py'),
    FIRST_APP_PATH / Path('tasks.py'),
]


if __name__ == '__main__':
    if '{{ cookiecutter.include_sample_content }}' == 'n':
        for path in SAMPLE_MODEL_FILES:
            os.remove(os.path.join(PROJECT_DIRECTORY, path))
