from allauth.account.adapter import DefaultAccountAdapter


class EmailAsUsernameAccountAdapter(DefaultAccountAdapter):
    """Automatically populate the username as the email address."""

    def populate_username(self, request, user):
        user.username = user.email
