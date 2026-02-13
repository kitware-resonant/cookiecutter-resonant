# cookiecutter-resonant

# Creation
* [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/)
* Run: `uvx copier copy --trust gh:kitware-resonant/cookiecutter-resonant <local-path-to-new-project>`
  * This will create a new directory for you.
* Within `<local-path-to-new-project>`, initialize Git and connect it to your upstream repository.

## With `include_example_code`
If `include_example_code` is enabled, some initial models, templates, and an associated migration
are included, as an example of a simple project's structure and capabilities.

Once you've adapted the example code to your own project's needs, you should **delete**
`{{ python_package_name }}/{{ core_app_name }}/migrations/0002_initial_models.py` 
and run `./manage.py makemigrations` to create a new initial migration for your actual models.
Otherwise, the example models will be permanently included in the migration history.

## Without `include_example_code`
If `include_example_code` is disabled, you may wish to make some small changes as your project
grows.

Once pytest tests are added, add / uncomment `envlist = test` in
`{{ project_slug }}/tox.ini`.

# Update
To update an existing project, run:
`uvx copier update -a .copier-answers.resonant.yml -A --trust`
