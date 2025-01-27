"""
Configure Django's email sending.

The following environment variables must be externally set:
* `DJANGO_EMAIL_URL`, as a URL for login to an STMP server, as parsed by `dj-email-url`. This
  typically will start with `submission:`. Special characters in passwords must be URL-encoded.
  See https://pypi.org/project/dj-email-url/ for full details.
* `DJANGO_DEFAULT_FROM_EMAIL`, as the default From address for outgoing email.
"""

from resonant_settings._env import env

vars().update(env.email_url("DJANGO_EMAIL_URL"))

DEFAULT_FROM_EMAIL: str = env.str("DJANGO_DEFAULT_FROM_EMAIL")
SERVER_EMAIL = DEFAULT_FROM_EMAIL
