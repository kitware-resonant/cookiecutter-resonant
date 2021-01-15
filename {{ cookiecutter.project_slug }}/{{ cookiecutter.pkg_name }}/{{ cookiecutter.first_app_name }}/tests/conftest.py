import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

{% if cookiecutter.include_example_code == 'Y' -%}
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


{% if cookiecutter.include_example_code == 'Y' -%}
register(ImageFactory)
{% endif -%}
register(UserFactory)
