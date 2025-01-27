from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.models import AbstractUser
from django.http import HttpRequest


class EmailAsUsernameAccountAdapter(DefaultAccountAdapter):
    """Automatically populate the username as the email address."""

    def populate_username(self, request: HttpRequest, user: AbstractUser) -> None:
        user.username = user.email
