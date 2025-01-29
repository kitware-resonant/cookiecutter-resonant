from __future__ import annotations

from datetime import timedelta
from pathlib import Path

from environ import Env
from resonant_settings.allauth import *
from resonant_settings.celery import *
from resonant_settings.debug_toolbar import *
from resonant_settings.django import *
from resonant_settings.logging import *
from resonant_settings.oauth_toolkit import *
from resonant_settings.rest_framework import *

env = Env()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

WSGI_APPLICATION = '{{ cookiecutter.pkg_name }}.wsgi.application'
ROOT_URLCONF = '{{ cookiecutter.pkg_name }}.urls'

INSTALLED_APPS = [
    # Install local apps first, to ensure any overridden resources are found first
    '{{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.apps.{{ cookiecutter.first_app_name.split('_')|map('capitalize')|join('') }}Config',
    # Apps with overrides
    'auth_style',
    'resonant_settings.allauth_support',
    # Everything else
    'allauth',
    'allauth.account',
    'allauth.mfa',
    'allauth.socialaccount',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_filters',
    'drf_yasg',
    'oauth2_provider',
    'resonant_utils',
    'rest_framework',
    'rest_framework.authtoken',
    's3_file_field',
]

MIDDLEWARE = [
    # CorsMiddleware must be added before other response-generating middleware,
    # so it can potentially add CORS headers to those responses too.
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoiseMiddleware must be directly after SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# Internal datetimes are timezone-aware, so this only affects rendering and form input
TIME_ZONE = 'UTC'

DATABASES = {
    'default': {
        **env.db_url('DJANGO_DATABASE_URL', engine='django.db.backends.postgresql'),
        'CONN_MAX_AGE': timedelta(minutes=10).total_seconds(),
    }
}

STORAGES = {
    # Inject the default storage in particular run configurations
    'default': None,
    'staticfiles': {
        # CompressedManifestStaticFilesStorage does not work properly with drf-
        # https://github.com/axnsan12/drf-yasg/issues/761
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

STATIC_ROOT = BASE_DIR / 'staticfiles'
# Django staticfiles auto-creates any intermediate directories, but do so here to prevent warnings.
STATIC_ROOT.mkdir(exist_ok=True)

# Django's docs suggest that STATIC_URL should be a relative path,
# for convenience serving a site on a subpath.
STATIC_URL = 'static/'

# Make Django and Allauth redirects consistent, but both may be changed.
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

CORS_ORIGIN_WHITELIST: list[str] = env.list('DJANGO_CORS_ORIGIN_WHITELIST', cast=str, default=[])
CORS_ORIGIN_REGEX_WHITELIST: list[str] = env.list(
    'DJANGO_CORS_ORIGIN_REGEX_WHITELIST', cast=str, default=[]
)
