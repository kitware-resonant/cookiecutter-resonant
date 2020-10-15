# cookiecutter-django-girder

Usage: `cookiecutter https://github.com/girder/cookiecutter-django-girder.git`

## Delete example model migration

The cookiecutter includes some initial models and an associated migration,
as an example of how models should be written.

After you have created your first models and are ready to commit your code, you should **delete**
`{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/migrations/0002_initial_models.py`
and run `./manage.py makemigrations` to create a new initial migration for your actual models.
Otherwise, the example models will be permanently included in the migration history.
