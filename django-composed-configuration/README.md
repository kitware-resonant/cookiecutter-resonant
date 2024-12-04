# django-composed-configuration
[![PyPI](https://img.shields.io/pypi/v/django-composed-configuration)](https://pypi.org/project/django-composed-configuration/)

Turnkey Django settings for data management applications.

## Installation
Add to your project's requirements:
```
django-composed-configuration[dev,prod]
```

In your project's `settings.py`:
```python
from composed_configuration import (
    ComposedConfiguration,
    ConfigMixin,
    DevelopmentBaseConfiguration,
    ProductionBaseConfiguration,
)


class _ProjectMixin(ConfigMixin):
    # Define additional project-specific settings or overrides here
    pass

    @staticmethod
    def mutate_configuration(configuration: ComposedConfiguration) -> None:
        # Perform any non-overriding mutation of existing settings here
        # The "configuration" variable contains the flattened settings
        # For example:
        #   configuration.INSTALLED_APPS += ['my_extra_app']
        pass


class DevelopmentConfiguration(_ProjectMixin, DevelopmentBaseConfiguration):
    pass


class ProductionConfiguration(_ProjectMixin, ProductionBaseConfiguration):
    pass
```

At runtime:
* continue to set the `DJANGO_SETTINGS_MODULE` environment variable (pointing to `settings.py`)
* also set `DJANGO_CONFIGURATION`, with a value of
  either `DevelopmentConfiguration` or `ProductionConfiguration`
