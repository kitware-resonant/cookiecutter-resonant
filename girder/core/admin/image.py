from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin
from django.db.models import QuerySet
from django.http import HttpRequest
from django_admin_display import admin_display

from girder.core.models import Image
from girder.core.tasks import image_compute_checksum


class _ImageChecksumExistsFilter(admin.SimpleListFilter):
    title = 'checksum computed'
    parameter_name = 'checksum_exists'

    def lookups(self, request: HttpRequest, model_admin: ModelAdmin):
        return [('yes', 'Yes'), ('no', 'No')]

    def queryset(self, request: HttpRequest, queryset: QuerySet) -> QuerySet:
        value = self.value()
        if value == 'yes':
            return queryset.filter(checksum__isnull=False)
        elif value == 'no':
            return queryset.filter(checksum__isnull=True)
        return queryset


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_checksum', 'created', 'owner']
    list_display_links = ['id', 'name']
    list_filter = [
        _ImageChecksumExistsFilter,
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

    @admin_display(
        short_description='Checksum prefix',
        empty_value_display='Not computed',
        # Sorting by checksum also sorts the prefix values
        admin_order_field='checksum',
    )
    def short_checksum(self, image: Image):
        return image.short_checksum

    @admin_display(short_description='Recompute checksum')
    def compute_checksum(self, request: HttpRequest, queryset: QuerySet):
        for image in queryset:
            image_compute_checksum.delay(image.pk)
        self.message_user(request, f'{len(queryset)} images queued', messages.SUCCESS)
