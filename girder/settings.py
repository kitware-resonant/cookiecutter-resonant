from pathlib import Path

from django_girders.configuration import DevelopmentBaseConfiguration


class DevelopmentConfiguration(DevelopmentBaseConfiguration):
    WSGI_APPLICATION = 'girder.wsgi.application'
    ROOT_URLCONF = 'girder.urls'

    BASE_DIR = str(Path(__file__).absolute().parent.parent)

    # TODO: INSTALLED_APPS
