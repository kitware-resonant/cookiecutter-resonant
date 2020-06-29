{% if cookiecutter.include_sample_content == 'Y' -%}
from .image import ImageAdmin

__all__ = ['ImageAdmin']
{% endif -%}
