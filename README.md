# {{ project_slug }}

## Develop with Docker (recommended)

This is the simplest configuration for developers to start with.
### Initial Setup
1. Run `docker-compose run --rm django ./manage.py migrate`
2. Run `docker-compose run --rm django ./manage.py createsuperuser` and follow the prompts to create your own user

### Run Application
1. Run `docker-compose up`
2. When finished, use `Ctrl+C`

### Application Maintenance
Occasionally, new package dependencies or schema changes will necessitate
maintenance. To non-destructively update your development stack at any time:
1. Run `docker-compose pull`
2. Run `docker-compose build`
3. Run `docker-compose run --rm django ./manage.py migrate`

## Develop Natively (advanced)
This configuration still uses Docker to run attached services in the background,
but allows developers to run the Python code on their native system.

### Initial Setup
1. Run `docker-compose -f ./docker-compose.yml up -d`
2. Install Python 3.8
3. Install [`psycopg2` build prerequisites](https://www.psycopg.org/docs/install.html#build-prerequisites)
4. Create and activate a new Python virtualenv
5. Run `pip install -e .`
6. Run `source ./dev/source-native-env.sh`
7. Run `./manage.py migrate`
8. Run `./manage.py createsuperuser` and follow the prompts to create your own user

### Run Application
1. Run (in separate windows) both:
   1. `./manage.py runserver`
   2. `celery worker --app {{ pkg_name }}.celery --loglevel info --without-heartbeat`
2. When finished, run `docker-compose stop`


TODO: Document:
  DOCKER_POSTGRES_PORT (with DJANGO_DATABASE_URL)
  DOCKER_RABBITMQ_PORT
  DOCKER_MINIO_PORT


## Testing
### Initial Setup
Tox is required to execute all tests.
It may be installed with `pip install tox`.

### Running Tests
Run `tox` to launch the full test suite.

Individual test environments may be selectively run.
This also allows additional options to be be added.
Useful sub-commands include:
* `tox -e lint`: Run only the style checks.
* `tox -e type`: Run only the type checks.
* `tox -e test`: Run only the unit tests.

To automatically reformat all code to comply with
some (but not all) of the style checks, run `tox -e format`.
