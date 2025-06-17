import logging
from typing import Any

from allauth.account.models import EmailAddress
from django.contrib.auth.models import AbstractUser

logger = logging.getLogger(__file__)


def verify_email_address_on_user_post_save(
    sender: type[AbstractUser],
    instance: AbstractUser,
    created: bool,
    **kwargs: Any,
) -> None:
    """Automatically verify email addresses of newly created superusers."""
    # These should always be true, but it's a final sanity check
    if created and instance.is_superuser:
        # Django is less strict than Allauth about duplicate email addresses (Django lowercases
        # the domain portion or an address, Allauth lowercases the whole address). It's possible
        # an acceptable email address via createsuperuser would be refused as a duplicate via
        # Allauth.
        # It's also possible that in an mature database where users have multiple non-primary
        # emails, the new user's email matches an existing user's non-primary email, violating
        # uniqueness.
        # So, make a conservative effort at setting the email address as verified, since failure is
        # not critical and can be resolved by the user.
        email_address, created = EmailAddress.objects.get_or_create(
            email__iexact=instance.email,
            defaults={
                "user": instance,
                "email": instance.email,
                "verified": True,
                "primary": True,
            },
        )
        if not created:
            logger.warning(f'Could not automatically verify email address "{instance.email}".')
