{% if cookiecutter.include_example_code == 'Y' -%}
from .image import ImageViewSet

__all__ = ['ImageViewSet']
{% endif -%}
