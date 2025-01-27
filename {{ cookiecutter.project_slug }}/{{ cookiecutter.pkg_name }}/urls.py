from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI

{% if cookiecutter.include_example_code == 'yes' -%}
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.views import GalleryView, image_summary

{% endif -%}

api = NinjaAPI()

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('oauth/', include('oauth2_provider.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/s3-upload/', include('s3_file_field.urls')),
    path('api/v1/', api.urls),
{%- if cookiecutter.include_example_code == 'yes' %}
    path('summary/', image_summary, name='image-summary'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
{%- endif %}
]

if settings.DEBUG:
    import debug_toolbar.toolbar

    urlpatterns += [
        *debug_toolbar.toolbar.debug_toolbar_urls(),
        path('__reload__/', include('django_browser_reload.urls')),
    ]
