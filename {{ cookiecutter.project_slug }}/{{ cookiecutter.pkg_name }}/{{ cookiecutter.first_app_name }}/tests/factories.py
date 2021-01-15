from django.contrib.auth.models import User
import factory.django
{% if cookiecutter.include_example_code == 'yes' %}
from {{ cookiecutter.pkg_name }}.{{ cookiecutter.first_app_name }}.models import Image
{% endif %}

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.SelfAttribute('email')
    email = factory.Faker('safe_email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
{% if cookiecutter.include_example_code == 'yes' %}

class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image

    name = factory.Faker('file_name', category='image')
    blob = factory.django.FileField(data=b'fakeimagebytes', filename='fake.png')
    owner = factory.SubFactory(UserFactory)
{% endif -%}
