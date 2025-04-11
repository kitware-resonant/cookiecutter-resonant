"""
Configure Django REST framework and drf-yasg.

This requires the `django-oauth-toolkit` and `drf-yasg` packages to be installed.
"""

from typing import Any

# When SessionAuthentication is allowed, it's critical that the following settings
# (respectively part of Django and django-cors-headers) are set to these values (although those
# are the also the default values).
SESSION_COOKIE_SAMESITE = "Lax"
CORS_ALLOW_CREDENTIALS = False

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        # Allow SessionAuthentication, as this is much more convenient for Ajax requests
        # from server-rendered pages, including:
        # * YASG (Swagger / ReDoc)
        # * The Admin interface, when using interactive fields like S3-file-field
        # * Augmentation of server-rendered views with background Javascript
        #   (see https://docs.djangoproject.com/en/3.1/ref/csrf/#ajax )
        # It's important that true SPAs and other clients be forced to go though
        # OAuth2Authentication instead, as this is the only supported auth mechanism which
        # robustly works across origins; however, it turns out that this can only be enforced
        # partially.
        # To understand why, first read https://web.dev/same-site-same-origin/ to understand
        # that even with "SameSite=Lax" (or "SameSite=Strict"), cookies are only technically
        # limited to same-site requests, and do not have the stronger same-origin limitation.
        # If a naive SPA developer configures their client to include credentials
        # ("{withCredentials: true}" in XHR, jQuery, and Axios, or "{credentials: 'include'}"
        # in Fetch; this configuration is often suggested as an "easy" fix for authentication
        # problems by StackOverflow), then the session cookie will be sent with any cross-site
        # requests where the user has logged into the Django server. Note, cross-site requests
        # include origins with a different port (typical in local development) and origins with
        # a different subdomain (common in many deployments). From DRF's perspective, as long
        # as the request uses a safe verb (more on this below), the request will be
        # authenticated transparently. However, since Django is configured to not set
        # "Access-Control-Allow-Credentials", the SPA client will not be able to read the
        # response and get a CORS error; this is the right outcome (client cannot effectively
        # make the request), but with a confusing and hard-to-debug reason (CORS error,
        # instead of a 401/403) and developers may be tempted to "fix" it by enabling
        # "Access-Control-Allow-Credentials" instead of fixing their client to use OAuth
        # correctly, which will likely lead to further bugs when the SPA is deployed to a
        # non-same-site environment. Alternatively, if the request does not use a safe verb
        # (and the request is not preflighted by the browser, which is permitted in some
        # cases), DRF will enforce CSRF protection and the request will 403 fail with a
        # "CSRF Failed: CSRF token missing or incorrect" message, which is also confusing and
        # may lead developers to incorrect fixes.
        # TL;DR: Developers of SPAs may encounter misleading error messages when making Ajax
        # requests "withCredentials", but security is still maintained.
        "rest_framework.authentication.SessionAuthentication",
    ],
    # This is a much more sensible degree of basic security
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticatedOrReadOnly"],
    # BoundedLimitOffsetPagination provides LimitOffsetPagination with a maximum page size
    "DEFAULT_PAGINATION_CLASS": "resonant_utils.rest_framework.BoundedLimitOffsetPagination",
    # This provides a sane default for requests that do not specify a page size.
    # This also ensures that endpoints with pagination will always return a
    # pagination-structured response.
    "PAGE_SIZE": 100,
    # Real clients typically JSON-encode their request bodies, so the test client should too
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

SWAGGER_SETTINGS: dict[str, Any] = {
    # The default security definition ("basic") is not supported by this DRF configuration,
    # so expect all logins to come via the Django session, which there's no OpenAPI
    # security definition for.
    "SECURITY_DEFINITIONS": None,
    "USE_SESSION_AUTH": True,
    # Needed because https://github.com/axnsan12/drf-yasg/pull/911
    "USE_COMPAT_RENDERERS": False,
}

REDOC_SETTINGS: dict[str, Any] = {}
