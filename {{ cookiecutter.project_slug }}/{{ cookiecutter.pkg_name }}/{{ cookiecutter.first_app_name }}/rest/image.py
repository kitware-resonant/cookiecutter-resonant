from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
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

    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['name', 'checksum']

    pagination_class = PageNumberPagination

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        image = get_object_or_404(Image, pk=pk)
        return HttpResponseRedirect(image.blob.url)

    @action(detail=True, methods=['post'])
    def compute(self, request, pk=None):
        # Ensure that the image exists, so a non-existent pk isn't dispatched
        image = get_object_or_404(Image, pk=pk)
        image_compute_checksum.delay(image.pk)
        return Response('', status=status.HTTP_202_ACCEPTED)
