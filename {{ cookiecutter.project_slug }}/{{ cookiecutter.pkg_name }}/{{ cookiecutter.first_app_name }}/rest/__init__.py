{% if cookiecutter.example_models == 'yes' -%}
from .image import ImageViewSet

__all__ = ['ImageViewSet']
{%- endif %}
