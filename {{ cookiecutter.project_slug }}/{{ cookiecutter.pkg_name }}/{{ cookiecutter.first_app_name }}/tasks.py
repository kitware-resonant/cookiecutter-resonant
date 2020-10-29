from celery import shared_task

from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.models import Image


@shared_task()
def image_compute_checksum(image_pk: int):
    image = Image.objects.get(pk=image_pk)
    image.compute_checksum()
    image.save()
