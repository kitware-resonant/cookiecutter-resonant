"""Configure Django's security middleware to use and require HTTPS."""

from datetime import timedelta

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Enable HSTS
SECURE_HSTS_SECONDS = int(timedelta(days=365).total_seconds())
# This is already False by default, but it's important to ensure HSTS is not forced on other
# subdomains which may have different HTTPS practices.
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
# This is already False by default, but per https://hstspreload.org/#opt-in, projects should
# opt-in to preload by overriding this setting. Additionally, all subdomains must have HSTS to
# register for preloading.
SECURE_HSTS_PRELOAD = False

__all__ = [
    "SECURE_SSL_REDIRECT",
    "SESSION_COOKIE_SECURE",
    "CSRF_COOKIE_SECURE",
    "SECURE_HSTS_SECONDS",
    "SECURE_HSTS_INCLUDE_SUBDOMAINS",
    "SECURE_HSTS_PRELOAD",
]
