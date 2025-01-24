"""
Configure Django OAuth Toolkit with the following features:
* Harden security
* Improve usability of token scopes
* Improve quality of live for out of band flows and non-refreshing clients

This requires the `django-oauth-toolkit` package to be installed.
"""

from datetime import timedelta

OAUTH2_PROVIDER = {
    "ALLOWED_REDIRECT_URI_SCHEMES": ["https"],
    # Don't require users to re-approve scopes each time
    "REQUEST_APPROVAL_PROMPT": "auto",
    # ERROR_RESPONSE_WITH_SCOPES is only used with the "permission_classes" helpers for scopes.
    # If the scope itself is confidential, this could leak information. but the usability
    # benefit is probably worth it.
    "ERROR_RESPONSE_WITH_SCOPES": True,
    # Allow 5 minutes for a flow to exchange an auth code for a token. This is typically
    # 60 seconds but out-of-band flows may take a bit longer. A maximum of 10 minutes is
    # recommended: https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.
    "AUTHORIZATION_CODE_EXPIRE_SECONDS": timedelta(minutes=5).total_seconds(),
    # Django can persist logins for longer than this via cookies,
    # but non-refreshing clients will need to redirect to Django's auth every 24 hours.
    "ACCESS_TOKEN_EXPIRE_SECONDS": timedelta(days=1).total_seconds(),
    # This allows refresh tokens to eventually be removed from the database by
    # "manage.py cleartokens". This value is not actually enforced when refresh tokens are
    # checked, but it can be assumed that all clients will need to redirect to Django's auth
    # every 30 days.
    "REFRESH_TOKEN_EXPIRE_SECONDS": timedelta(days=30).total_seconds(),
}
