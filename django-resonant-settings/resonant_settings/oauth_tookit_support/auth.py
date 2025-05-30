from __future__ import annotations

from typing import Callable

from ninja.security import HttpBearer, django_auth
from oauth2_provider.oauth2_backends import get_oauthlib_core

ACCESS_PERMS = ["any", "is_authenticated", "is_staff"]


class OAuth2AuthBearer(HttpBearer):
    def __init__(self, perm: str):
        if perm not in ACCESS_PERMS:
            raise ValueError(f"Invalid permission: {perm}")
        self.perm = perm
        super().__init__()

    # This is a reimplementation of the django-oauth-toolkit authentication backend for DRF.
    # See https://github.com/jazzband/django-oauth-toolkit/blob/a4ae1d4716bcabe45d80a787f4064022f11e584f/oauth2_provider/contrib/rest_framework/authentication.py#L8  # noqa: E501
    def authenticate(self, request, token):
        oauthlib_core = get_oauthlib_core()
        valid, r = oauthlib_core.verify_request(request, scopes=[])

        if valid:
            # See https://github.com/vitalik/django-ninja/issues/76 for why we have to manually set
            # request.user here.
            request.user = r.user

            if self.perm == "any":
                return r.user, token
            if self.perm == "is_authenticated" and r.user.is_authenticated:
                return r.user, token
            if self.perm == "is_staff" and r.user.is_authenticated and r.user.is_staff:
                return r.user, token
        elif self.perm == "any":
            return True
        else:
            request.oauth2_error = getattr(r, "oauth2_error", {})


# The lambda _: True is to handle the case where a user doesn't pass any authentication.
allow_any: list[Callable] = [django_auth, OAuth2AuthBearer("any"), lambda _: True]
is_authenticated = [django_auth, OAuth2AuthBearer("is_authenticated")]
is_staff = [OAuth2AuthBearer("is_staff")]
