import iptools

from .testing import *

# Import these afterwards, to override
from resonant_settings.development.celery import *  # isort: skip
from resonant_settings.development.extensions import *  # isort: skip

INSTALLED_APPS += [
    'debug_toolbar',
    'django_browser_reload',
    'django_extensions',
]
# Force WhiteNoice to serve static files, even when using 'manage.py runserver'
staticfiles_index = INSTALLED_APPS.index('django.contrib.staticfiles')
INSTALLED_APPS.insert(staticfiles_index, 'whitenoise.runserver_nostatic')

# Include Debug Toolbar middleware as early as possible in the list.
# However, it must come after any other middleware that encodes the response’s content,
# such as GZipMiddleware.
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
# Should be listed after middleware that encode the response.
MIDDLEWARE += [
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

# DEBUG is not enabled for testing, to maintain parity with production.
# Also, do not directly reference DEBUG when toggling application features; it's more sustainable
# to add new settings as individual feature flags.
DEBUG = True

# This is typically only overridden when running from Docker.
INTERNAL_IPS = iptools.IpRangeList(
    *env.list('DJANGO_INTERNAL_IPS', cast=str, default=['127.0.0.1'])
)
CORS_ORIGIN_REGEX_WHITELIST = env.list(
    'DJANGO_CORS_ORIGIN_REGEX_WHITELIST',
    cast=str,
    default=[r'^http://localhost:\d+$', r'^http://127\.0\.0\.1:\d+$'],
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

OAUTH2_PROVIDER['ALLOWED_REDIRECT_URI_SCHEMES'] = ['http', 'https']
# In development, always present the approval dialog
OAUTH2_PROVIDER['REQUEST_APPROVAL_PROMPT'] = 'force'

SHELL_PLUS_IMPORTS = [
    'from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }} import tasks',
]
