{% if cookiecutter.example_models == 'yes' -%}
from .image import ImageAdmin

__all__ = ['ImageAdmin']
{% endif -%}
