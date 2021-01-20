{% if cookiecutter.include_example_code == 'yes' -%}
from .image import ImageViewSet

__all__ = ['ImageViewSet']
{% endif -%}
