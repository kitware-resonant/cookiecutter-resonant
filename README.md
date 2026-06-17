# cookiecutter-resonant

# Creation
* [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/) and
  [the GitHub CLI](https://github.com/cli/cli#installation)
* Run:
  ```shell
  uvx copier copy https://github.com/kitware-resonant/cookiecutter-resonant <new-project-path>
  ```
  * This will create a new directory at `<new-project-path>` for you.
* Initialize uv and Git:
  ```shell
  cd <new-project-path>`
  uv lock
  git init && git add -A && git commit -m 'Initial commit'
  ```
* Push to a new GitHub repository:
  ```shell
  gh repo create <org>/<repo-name> --private -s . --push
  ```

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
`{{ python_package_name }}/tox.ini`.

# Update
To update an existing project, run:
```shell
uvx copier update -a .copier-answers.resonant.yml -A
```
