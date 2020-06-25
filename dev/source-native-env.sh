# This file must be sourced, not run
dotenv_file="$( dirname "${BASH_SOURCE[0]}" )/.env.docker-compose-native"
while read -r var; do
  export "${var?}"
done < "${dotenv_file}"
