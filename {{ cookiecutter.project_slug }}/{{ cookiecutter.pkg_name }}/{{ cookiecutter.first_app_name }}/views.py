from django.contrib.auth.models import User  # noqa: F401
from django.db.models import Count, Q  # noqa: F401
from django.shortcuts import render  # noqa: F401
from django.views.generic import ListView  # noqa: F401
{% if cookiecutter.include_example_code == 'yes' %}
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
