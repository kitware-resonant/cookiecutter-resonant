terraform {
  required_version = ">= 1.1"

  backend "remote" {
    organization = "{{ cookiecutter.project_slug }}"

    workspaces {
      name = "{{ cookiecutter.project_slug }}"
    }
  }

  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
    heroku = {
      source = "heroku/heroku"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  # Must set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY envvars
}
provider "heroku" {
  # Must set HEROKU_EMAIL, HEROKU_API_KEY envvars
}
