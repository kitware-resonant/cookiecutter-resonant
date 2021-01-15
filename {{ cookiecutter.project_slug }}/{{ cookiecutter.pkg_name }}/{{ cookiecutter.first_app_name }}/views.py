{% if cookiecutter.include_example_code == 'Y' -%}
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import render
from django.views.generic import ListView

from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.models import Image


class GalleryView(ListView):
    queryset = Image.objects.order_by('created')
    template_name = 'gallery.html'
    paginate_by = 20


def image_summary(request):
    return render(
        request,
        'summary.html',
        {
            'user_summary': User.objects.annotate(
                processed_images=Count('image', filter=Q(image__checksum__isnull=False)),
                unprocessed_images=Count('image', filter=Q(image__checksum__isnull=True)),
            )
        },
    )
{% endif -%}
