from __future__ import annotations

from typing import TYPE_CHECKING

from allauth.account import app_settings as allauth_settings
from django.contrib.auth import get_user_model
from django.contrib.auth.management.commands import createsuperuser as django_createsuperuser
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from resonant_settings.allauth_support import createsuperuser as allauth_support_createsuperuser
from resonant_settings.allauth_support.receiver import verify_email_address_on_user_post_save

if TYPE_CHECKING:
    from django.contrib.auth.base_user import AbstractBaseUser
    from django.core.management import BaseCommand

"""
When Allauth is configured to use a User's `email` as the `username`, override the `createsuperuser`
management command to only prompt for an email address.
"""

username_required: bool | None = allauth_settings.SIGNUP_FIELDS.get("username", {}).get(
    "required", None
)

Command: type[BaseCommand]
user_model: type[AbstractBaseUser]
# If using email as username
if not username_required:
    # Expose the modified command
    Command = allauth_support_createsuperuser.Command
    # `create_superuser` always saves a `User` instance (not `EmailAsUsernameProxyUser`),
    # so `post_save` fires with `sender=User`.
    user_model = User

else:
    # Expose the pristine upstream version of the command
    Command = django_createsuperuser.Command
    user_model = get_user_model()

# Always automatically verify email addresses of newly created superusers
post_save.connect(verify_email_address_on_user_post_save, sender=user_model)
