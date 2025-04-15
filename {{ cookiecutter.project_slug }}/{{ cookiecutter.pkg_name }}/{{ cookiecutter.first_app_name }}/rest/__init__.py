{% if cookiecutter.include_example_code == 'yes' -%}
from .image import router as image_router

__all__ = ['image_router']
{% endif -%}
