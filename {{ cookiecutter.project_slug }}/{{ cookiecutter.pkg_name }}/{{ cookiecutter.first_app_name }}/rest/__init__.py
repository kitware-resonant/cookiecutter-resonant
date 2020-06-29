{% if cookiecutter.include_sample_content == 'Y' -%}
from .image import ImageViewSet

__all__ = ['ImageViewSet']
{% endif -%}
