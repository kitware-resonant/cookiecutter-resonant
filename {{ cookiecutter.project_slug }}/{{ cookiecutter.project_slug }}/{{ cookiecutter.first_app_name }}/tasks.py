from celery import shared_task

from {{ pkg_name }}.{{ first_app_name }}.models import Image


@shared_task()
def image_compute_checksum(image_id: int):
    image = Image.objects.get(pk=image_id)
    image.checksum = image.compute_checksum()
    image.save()
