# This file must be sourced, not run
DOTENV_FILE="$( dirname "${BASH_SOURCE[0]}" )/.env.docker-compose-native"

# This is a hack to make sourcing source-native-env.sh compliant with ZSH
# See: https://github.com/girder/cookiecutter-django-girder/issues/1
if [[ ! -r $DOTENV_FILE ]]; then
  DOTENV_FILE=$( dirname $0:A )/.env.docker-compose-native
  if [[ ! -r $DOTENV_FILE ]]; then
    echo >&2 "Could not find .env.docker-compose-native, try sourcing $0 from the dev/ directory."
    return
  fi
fi

while read -r VAR; do
  export "${VAR?}"
done < "${DOTENV_FILE}"
