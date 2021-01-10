from celery import shared_task

{% if cookiecutter.example_models == 'yes' -%}
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.models import Image


@shared_task()
def image_compute_checksum(image_id: int):
    image = Image.objects.get(pk=image_id)
    image.compute_checksum()
    image.save()
{% endif -%}
