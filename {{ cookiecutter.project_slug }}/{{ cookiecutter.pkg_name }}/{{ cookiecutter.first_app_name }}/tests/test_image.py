import pytest

from .factories import ImageFactory


def test_image_checksum():
    # Use "build" strategy, so database is not required
    image = ImageFactory.build()
    image.compute_checksum()
    assert image.checksum is not None


@pytest.mark.django_db
def test_image_rest_retrieve(api_client, image):
    resp = api_client.get(f'/api/v1/images/{image.id}/')
    assert resp.status_code == 200
    # Inspect .data to avoid parsing the response content
    assert resp.data['name'] == image.name
