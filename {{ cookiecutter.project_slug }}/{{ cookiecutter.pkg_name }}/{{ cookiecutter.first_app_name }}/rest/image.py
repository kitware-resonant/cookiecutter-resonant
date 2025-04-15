from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from ninja import FilterSchema, ModelSchema, Query
from ninja.pagination import RouterPaginated

from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.models import Image
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.rest.user import UserSchema
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.tasks import image_compute_checksum

router = RouterPaginated()


class ImageResponseSchema(ModelSchema):
    class Meta:
        model = Image
        fields = ['id', 'name', 'checksum', 'created', 'owner']
        read_only_fields = ['checksum', 'created']

    owner: UserSchema


class ImageFilterSchema(FilterSchema):
    name: str | None = None
    checksum: str | None = None


@router.get('/', response=list[ImageResponseSchema])
def list_images(request, filters: ImageFilterSchema = Query(...)):  # noqa: B008
    return Image.objects.all()


@router.get('/{int:pk}/', response=ImageResponseSchema)
def get_image(request, pk: int):
    return get_object_or_404(Image, pk=pk)


@router.get('/download/{int:pk}/')
def download_image(request, pk: int):
    image = get_object_or_404(Image, pk=pk)
    return HttpResponseRedirect(image.blob.url)


@router.post('/compute/{int:pk}/')
def compute_image(request, pk: int):
    # Ensure that the image exists, so a non-existent pk isn't dispatched
    image = get_object_or_404(Image, pk=pk)
    image_compute_checksum.delay(image.pk)
    return 202
