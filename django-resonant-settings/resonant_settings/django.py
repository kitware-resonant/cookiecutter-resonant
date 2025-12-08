"""Configure a basic Django project."""

from typing import Any

TEMPLATES: list[dict[str, Any]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

PASSWORD_HASHERS: list[str] = [
    # Argon2 is recommended by OWASP, so make it the default for new passwords
    # https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    # scrypt was the default hasher in older versions of Resonant,
    # so it must be enabled to read old passwords
    "django.contrib.auth.hashers.ScryptPasswordHasher",
    # Support for other hashers isn't needed,
    # since databases shouldn't have entries with other algorithms
]
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

__all__ = [
    "TEMPLATES",
    "PASSWORD_HASHERS",
    "AUTH_PASSWORD_VALIDATORS",
]
