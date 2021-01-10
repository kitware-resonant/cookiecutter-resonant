{% if cookiecutter.example_models == 'yes' -%}
from .image import Image

__all__ = ['Image']
{%- endif %}
