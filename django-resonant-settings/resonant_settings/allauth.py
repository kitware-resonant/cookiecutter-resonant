"""
Configure django-allauth with the following features:
* Disable usernames for end users, using exclusively email addresses for login
* Require email verification
* Quality of life improvements for users

This requires the `django-allauth` package to be installed and requires
`resonant_settings.allauth_support` to be added to INSTALLED_APPS.
"""

# The sites framework requires this to be set.
# In the unlikely case where a database's pk sequence for the django_site table is not reset,
# the default site object could have a different pk. Then this will need to be overridden
# downstream.
SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Django's built-in ModelBackend is not necessary, since all users will be
    # authenticated by their email address
    "allauth.account.auth_backends.AuthenticationBackend",
]

# see configuration documentation at
#   https://django-allauth.readthedocs.io/en/latest/configuration.html

# Require email verification
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# Use email as the identifier for login
ACCOUNT_LOGIN_METHODS = {"email"}
# Don't require a username, but make email required
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

# Set the username as the email
ACCOUNT_ADAPTER = "resonant_settings.allauth_support.adapter.EmailAsUsernameAccountAdapter"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

# Quality of life improvements, but may not work if the browser is closed
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# Confirm URLs include a secret token, so CSRF safety isn't a concern
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

# This will likely become the default in the future, but enable it now
ACCOUNT_PRESERVE_USERNAME_CASING = False
