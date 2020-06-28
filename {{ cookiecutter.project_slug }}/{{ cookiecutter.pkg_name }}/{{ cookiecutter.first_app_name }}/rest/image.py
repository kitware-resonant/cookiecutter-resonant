from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.models import Image
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.rest.user import UserSerializer
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.tasks import image_compute_checksum


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'checksum', 'created', 'owner']
        read_only_fields = ['checksum', 'created']

    owner = UserSerializer()


class ImageViewSet(ReadOnlyModelViewSet):
    queryset = Image.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ImageSerializer

    pagination_class = PageNumberPagination

    @action(detail=True, methods=['post'])
    def compute(self, request, pk=None):
        # Ensure that the image exists, so a non-existent pk isn't dispatched
        image = get_object_or_404(Image, pk=pk)
        image_compute_checksum.delay(image.pk)
        return Response('', status=status.HTTP_202_ACCEPTED)
