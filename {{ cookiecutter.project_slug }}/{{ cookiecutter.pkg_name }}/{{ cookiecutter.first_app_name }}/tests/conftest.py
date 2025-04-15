from django.contrib.auth.models import User
from django.test import Client
import pytest

{% if cookiecutter.include_example_code == 'yes' -%}
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.models import Image

from .factories import ImageFactory, UserFactory
{%- else -%}

from .factories import UserFactory
{%- endif %}


@pytest.fixture
def client() -> Client:
    return Client()


@pytest.fixture
def authenticated_client(user: User) -> Client:
    client = Client()
    client.force_login(user=user)
    return client


{% if cookiecutter.include_example_code == 'yes' -%}
@pytest.fixture
def image() -> Image:
    return ImageFactory.create()


{% endif -%}
@pytest.fixture
def user() -> User:
    return UserFactory.create()
