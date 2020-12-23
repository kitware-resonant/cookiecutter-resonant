from django.contrib import admin

from .image import ImageAdmin

__all__ = ['ImageAdmin']

admin.site.site_header = '{{ cookiecutter.project_name }}'
admin.site.site_title = '{{ cookiecutter.project_name }}'
admin.site.index_title = ''
