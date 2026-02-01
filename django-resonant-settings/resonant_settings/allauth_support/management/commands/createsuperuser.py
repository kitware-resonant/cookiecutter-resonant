from __future__ import annotations

from typing import TYPE_CHECKING, cast

from allauth.account import app_settings as allauth_settings
from django.contrib.auth import get_user_model
from django.contrib.auth.management.commands import createsuperuser as django_createsuperuser
from django.db.models.signals import post_save

from resonant_settings.allauth_support import createsuperuser as allauth_support_createsuperuser
from resonant_settings.allauth_support.receiver import verify_email_address_on_user_post_save

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser
    from django.core.management import BaseCommand

"""
When Allauth is configured to use a User's `email` as the `username`, override the `createsuperuser`
management command to only prompt for an email address.
"""

username_required: bool | None = allauth_settings.SIGNUP_FIELDS.get("username", {}).get(
    "required", None
)

# If using email as username
if not username_required:
    # Expose the modified command
    Command: type[BaseCommand] = allauth_support_createsuperuser.Command
    user_model: type[AbstractUser] = allauth_support_createsuperuser.EmailAsUsernameProxyUser

else:
    # Expose the pristine upstream version of the command
    Command = django_createsuperuser.Command
    user_model = cast("type[AbstractUser]", get_user_model())

# Always automatically verify email addresses of newly created superusers
post_save.connect(verify_email_address_on_user_post_save, sender=user_model)
