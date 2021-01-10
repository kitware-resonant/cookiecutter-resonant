# This file must be sourced, not run
DOTENV_FILE="$( dirname "${BASH_SOURCE[0]}" )/.env.docker-compose-native"

# This is a hack to make sourcing source-native-env.sh compliant with shells
# like ZSH See: https://github.com/girder/cookiecutter-django-girder/issues/1
if [[ ! -r $DOTENV_FILE ]]; then
  if [[ -r dev/.env.docker-compose-native ]]; then
    DOTENV_FILE=dev/.env.docker-compose-native
  else
    echo >&2 "Could not find .env.docker-compose-native, are you sourcing from the root directory?"
    return
  fi
fi

while read -r VAR; do
  export "${VAR?}"
done < "${DOTENV_FILE}"
