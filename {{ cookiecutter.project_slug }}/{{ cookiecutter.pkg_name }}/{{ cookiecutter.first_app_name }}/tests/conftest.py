from django.contrib.auth.models import User
import pytest
from rest_framework.test import APIClient

{% if cookiecutter.include_example_code == 'yes' -%}
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.models import Image

from .factories import ImageFactory, UserFactory
{%- else -%}
from .factories import UserFactory
{%- endif %}


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def authenticated_api_client(user) -> APIClient:
    client = APIClient()
    client.force_authenticate(user=user)
    return client


{% if cookiecutter.include_example_code == 'yes' -%}
@pytest.fixture
def image() -> Image:
    return ImageFactory()


{% endif -%}
@pytest.fixture
def user() -> User:
    return UserFactory()
