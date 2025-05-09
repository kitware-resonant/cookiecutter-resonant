# {{ cookiecutter.project_name }}

## Develop with VSCode Dev Containers (recommended quickstart)

### Initial Setup
1. Follow the steps for [setting up Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers#_installation) if necessary.
1. From VSCode, use `Ctrl-Shift-p` and run the command `Dev Containers: Reopen in Container`.
1. From the VSCode built-in terminal, run `uv run ./manage.py migrate`.
1. From the VSCode built-in terminal, run `uv run ./manage.py createsuperuser`.

### Run Application
1. Run `serve` from the VSCode built-in-terminal.
1. Access the site, starting at http://localhost:8000/admin/
1. When finished, use `Ctrl+C`

## Develop with Docker
This is the simplest configuration for developers to start with.

### Initial Setup
1. Run `docker compose run --rm django ./manage.py migrate`
2. Run `docker compose run --rm django ./manage.py createsuperuser`
   and follow the prompts to create your own user

### Run Application
1. Run `docker compose up`
2. Access the site, starting at http://localhost:8000/admin/
3. When finished, use `Ctrl+C`

### Maintenance
To non-destructively update your development stack at any time:
1. Run `docker compose down`
2. Run `docker compose pull`
3. Run `docker compose build --pull`
4. Run `docker compose run --rm django ./manage.py migrate`

### Destruction
1. Run `docker compose down -v`

## Develop Natively (advanced)
This configuration still uses Docker to run attached services in the background,
but allows developers to run Python code on their native system.

### Initial Setup
1. Run `docker compose -f ./docker-compose.yml up -d`
2. [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/)
3. Run `export UV_ENV_FILE=./dev/.env.docker-compose-native`
4. Run `./manage.py migrate`
5. Run `./manage.py createsuperuser` and follow the prompts to create your own user

### Run Application
1. Ensure `docker compose -f ./docker-compose.yml up -d` is still active
2. Run `export UV_ENV_FILE=./dev/.env.docker-compose-native`
3. Run: `./manage.py runserver_plus`
4. Run in a separate terminal: `uv run celery --app {{ cookiecutter.pkg_name }}.celery worker --loglevel INFO --without-heartbeat`
5. When finished, run `docker compose stop`

## Testing
### Initial Setup
tox is used to manage the execution of all tests.
[Install `uv`](https://docs.astral.sh/uv/getting-started/installation/) and run tox with
`uv run tox ...`.

When running the "Develop with Docker" configuration, all tox commands must be run as
`docker compose run --rm django uv run tox`; extra arguments may also be appended to this form.

### Running Tests
Run `uv run tox` to launch the full test suite.

Individual test environments may be selectively run.
This also allows additional options to be be added.
Useful sub-commands include:
* `uv run tox -e lint`: Run only the style checks
* `uv run tox -e type`: Run only the type checks
* `uv run tox -e test`: Run only the pytest-driven tests

To automatically reformat all code to comply with
some (but not all) of the style checks, run `uv run tox -e format`.
