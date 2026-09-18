"""
Configure Django's email sending.

The following environment variables must be externally set:
* `DJANGO_EMAIL_URL`, as a URL for login to an STMP server, as parsed by `dj-email-url`. This
  typically will start with `submission:`. Special characters in passwords must be URL-encoded.
  See https://pypi.org/project/dj-email-url/ for full details.
* `DJANGO_DEFAULT_FROM_EMAIL`, as the default From address for outgoing email.
"""

from __future__ import annotations

from typing import Any

import django

from resonant_settings._env import env

email_config: dict[str, Any] = env.email_url("DJANGO_EMAIL_URL")

MAILERS: dict[str, dict[str, Any]] = {
    "default": {
        "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
        "OPTIONS": {
            "host": email_config["EMAIL_HOST"],
            "port": email_config["EMAIL_PORT"],
            "username": email_config["EMAIL_HOST_USER"],
            "password": email_config["EMAIL_HOST_PASSWORD"],
            "use_tls": email_config.get("EMAIL_USE_TLS", False),
            "use_ssl": email_config.get("EMAIL_USE_SSL", False),
        },
    },
}

DEFAULT_FROM_EMAIL: str = env.str("DJANGO_DEFAULT_FROM_EMAIL")
SERVER_EMAIL = DEFAULT_FROM_EMAIL

__all__ = [
    "DEFAULT_FROM_EMAIL",
    "MAILERS",
    "SERVER_EMAIL",
]

# TODO: Remove this when Django 6.0 support is dropped.
# Django 6.1 introduced `MAILERS` and deprecated the `EMAIL_*` settings, forbidding both from being
# defined together. Earlier versions of Django only understand the `EMAIL_*` settings.
if django.VERSION < (6, 1):
    EMAIL_BACKEND: str = MAILERS["default"]["BACKEND"]
    EMAIL_HOST: str = MAILERS["default"]["OPTIONS"]["host"]
    EMAIL_PORT: int = MAILERS["default"]["OPTIONS"]["port"]
    EMAIL_HOST_USER: str = MAILERS["default"]["OPTIONS"]["username"]
    EMAIL_HOST_PASSWORD: str = MAILERS["default"]["OPTIONS"]["password"]
    EMAIL_USE_TLS: bool = MAILERS["default"]["OPTIONS"]["use_tls"]
    EMAIL_USE_SSL: bool = MAILERS["default"]["OPTIONS"]["use_ssl"]

    __all__ += [
        "EMAIL_BACKEND",
        "EMAIL_HOST",
        "EMAIL_HOST_PASSWORD",
        "EMAIL_HOST_USER",
        "EMAIL_PORT",
        "EMAIL_USE_SSL",
        "EMAIL_USE_TLS",
    ]
