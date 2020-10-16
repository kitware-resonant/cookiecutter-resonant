from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions, routers

from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.rest import ImageViewSet
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.views import GalleryView, image_summary

router = routers.SimpleRouter()
router.register(r'images', ImageViewSet)

# OpenAPI generation
schema_view = get_schema_view(
    openapi.Info(title='{{ cookiecutter.project_name }}', default_version='v1', description=''),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/s3-upload/', include('s3_file_field.urls')),
    path('api/v1/', include(router.urls)),
    path('api/docs/redoc', schema_view.with_ui('redoc'), name='docs-redoc'),
    path('api/docs/swagger', schema_view.with_ui('swagger'), name='docs-swagger'),
    path('summary/', image_summary, name='image-summary'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
