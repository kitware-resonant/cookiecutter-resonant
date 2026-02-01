from __future__ import annotations

from typing import TYPE_CHECKING

from allauth.account.adapter import DefaultAccountAdapter

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser
    from django.http import HttpRequest


class EmailAsUsernameAccountAdapter(DefaultAccountAdapter):  # type: ignore[misc]
    """Automatically populate the username as the email address."""

    def populate_username(self, request: HttpRequest, user: AbstractUser) -> None:
        user.username = user.email
