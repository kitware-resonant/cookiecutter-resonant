# cookiecutter-girder-4

# Creation
* Install [`cookiecutter`](https://pypi.org/project/cookiecutter/)
* Run: `cookiecutter gh:girder/cookiecutter-girder-4`
  * Fill variables, as documented below.
  * This will create a new directory for you.
* In the new directory, initialize Git and connect it to your upstream repository.

## Variables
* `project_name`: A human-readable name for the project.
* `project_slug`: A PyPI package name, ideally dash-delimited.
* `pkg_name`: A Python module name (which must be underscore-delimited), used for the top-level Django project.
* `first_app_name`: A Python module name, used for the initial local Django app within this project. It's suggested that you use `core`, unless you know you will be creating multiple apps.
* `site_domain`: The fully-qualified domain name of the target production deployment. This must include a subdomain (e.g. `www`), as apex domains cannot be hosted on Heroku.
* `include_example_code`: Include (or exclude) example code for an "Image" management capability.

## Post-Creation Cleanup

### With `include_example_code`

If `include_example_code` is enabled, the cookiecutter includes some initial models, templates,
and an associated migration, as an example of a simple project's structure and capabilities.

Once you've adapted the example code to your own project's needs, you should **delete**
`{{ cookiecutter.pkg_name }}/{{ cookiecutter.first_app_name }}/migrations/0002_initial_models.py` 
and run `./manage.py makemigrations` to create a new initial migration for your actual models.
Otherwise, the example models will be permanently included in the migration history.

### Without `include_example_code`

If `include_example_code` is disabled, you may wish to make some small changes as your project
grows.

Once pytest tests are added, add / uncomment `envlist = test` in
`{{ cookiecutter.project_slug }}/tox.ini`.
