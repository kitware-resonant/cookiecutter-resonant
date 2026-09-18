"""Configure Django's security middleware to use and require HTTPS."""

from __future__ import annotations

from datetime import timedelta

from django.utils.csp import CSP

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

# Report-only CSP: logs violations without blocking anything, so projects can monitor and tighten.
# Override with SECURE_CSP to enforce.
SECURE_CSP_REPORT_ONLY: dict[str, list[str]] = {
    "default-src": [CSP.SELF],
}

__all__ = [
    "CSRF_COOKIE_SECURE",
    "SECURE_CSP_REPORT_ONLY",
    "SECURE_HSTS_INCLUDE_SUBDOMAINS",
    "SECURE_HSTS_PRELOAD",
    "SECURE_HSTS_SECONDS",
    "SECURE_SSL_REDIRECT",
    "SESSION_COOKIE_SECURE",
]
