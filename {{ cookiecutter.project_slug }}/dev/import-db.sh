#!/bin/bash
set -exu
set -o pipefail

export HEROKU_APP=TESTTESTTEST

DB_FILE=.db.pgdump
REUSE_LOCAL_DB_DUMP=0

while test $# -gt 0; do
    case "$1" in
        -h|--help)
            echo "import-db - Import a copy of the database locally"
            echo " "
            echo "import-db.sh [options]"
            echo " "
            echo "options:"
            echo "-h, --help                show brief help"
            echo "-r, --reuse               reuse an existing database dumped from this program (if possible)"
            exit 0
            ;;
        -r|--reuse)
            REUSE_LOCAL_DB_DUMP=1
            shift
            ;;
        *)
            break
            ;;
    esac
done


# Obtain database export
if [[ "$REUSE_LOCAL_DB_DUMP" -eq 1 && -s "$DB_FILE" ]]; then
    echo "Skipping database dump, reusing $DB_FILE"
else
    echo "Dumping production database"
    docker-compose exec postgres bash -c "pg_dump --format=custom --no-privileges $(heroku config:get DATABASE_URL)" > "$DB_FILE"
fi

# Drop/recreate database
docker-compose exec postgres bash -c "PGPASSWORD=postgres dropdb --host localhost --username postgres --if-exists django && createdb --host localhost --username postgres django"

# Import database dump
cat "$DB_FILE" | docker-compose exec -T -e PGPASSWORD=postgres postgres pg_restore --host localhost --username postgres --format=custom --no-privileges --no-owner --dbname=django

docker-compose restart

# Set every password to 'password' for local development
python manage.py set_fake_passwords
