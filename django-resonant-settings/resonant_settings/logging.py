"""
Configure Django logging with the following features:
* Emit all logs to stdout
* Exclude favicons and static files from request and server logs
* Improve log formatting and add colorization

This requires the `rich` package to be installed.
"""

import logging

from django.http import HttpRequest


def _filter_favicon_requests(record: logging.LogRecord) -> bool:
    if record.name == "django.request":
        request: HttpRequest | None = getattr(record, "request", None)
        if request and request.path == "/favicon.ico":
            return False

    if (
        record.name == "django.server"
        and isinstance(record.args, tuple)
        and len(record.args) >= 1
        and str(record.args[0]).startswith("GET /favicon.ico ")
    ):
        return False

    return True


def _filter_static_requests(record: logging.LogRecord) -> bool:
    if (
        record.name == "django.server"
        and isinstance(record.args, tuple)
        and len(record.args) >= 1
        and str(record.args[0]).startswith("GET /static/")
    ):
        return False

    return True


LOGGING = {
    "version": 1,
    # Replace existing logging configuration
    "incremental": False,
    # This redefines all of Django's declared loggers, but most loggers are implicitly
    # declared on usage, and should not be disabled. They often propagate their output
    # to the root anyway.
    "disable_existing_loggers": False,
    "formatters": {"rich": {"datefmt": "[%X]"}},
    "filters": {
        "filter_favicon_requests": {
            "()": "django.utils.log.CallbackFilter",
            "callback": _filter_favicon_requests,
        },
        "filter_static_requests": {
            "()": "django.utils.log.CallbackFilter",
            "callback": _filter_static_requests,
        },
    },
    "handlers": {
        "console": {
            "class": "rich.logging.RichHandler",
            "formatter": "rich",
            "filters": ["filter_favicon_requests", "filter_static_requests"],
        },
    },
    # Existing loggers actually contain direct (non-string) references to existing handlers,
    # so after redefining handlers, all existing loggers must be redefined too
    "loggers": {
        # Configure the root logger to output to the console
        "": {"level": "INFO", "handlers": ["console"], "propagate": False},
        # Django defines special configurations for the "django" and "django.server" loggers,
        # but we will manage all content at the root logger instead, so reset those
        # configurations.
        "django": {
            "handlers": [],
            "level": "NOTSET",
            "propagate": True,
        },
        "django.server": {
            "handlers": [],
            "level": "NOTSET",
            "propagate": True,
        },
    },
}
