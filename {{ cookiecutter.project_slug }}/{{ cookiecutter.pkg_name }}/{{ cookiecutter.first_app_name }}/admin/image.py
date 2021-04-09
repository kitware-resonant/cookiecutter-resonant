from django.contrib import admin, messages
from django.db.models import QuerySet
from django.http import HttpRequest

from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.models import Image
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.tasks import image_compute_checksum


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_checksum', 'created', 'owner']
    list_display_links = ['id', 'name']
    list_filter = [
        ('checksum', admin.EmptyFieldListFilter),
        ('created', admin.DateFieldListFilter),
        'owner__username',
    ]
    list_select_related = True
    # list_select_related = ['owner']

    search_fields = ['name']
    actions = ['compute_checksum']

    fields = ['name', 'blob', 'checksum', 'owner', 'created', 'modified']
    autocomplete_fields = ['owner']
    readonly_fields = ['checksum', 'created', 'modified']

    @admin.display(
        description='Checksum prefix',
        empty_value='Not computed',
        # Sorting by checksum also sorts the prefix values
        ordering='checksum',
    )
    def short_checksum(self, image: Image):
        return image.short_checksum

    @admin.action(description='Recompute checksum')
    def compute_checksum(self, request: HttpRequest, queryset: QuerySet):
        for image in queryset:
            image_compute_checksum.delay(image.pk)
        self.message_user(request, f'{len(queryset)} images queued', messages.SUCCESS)
