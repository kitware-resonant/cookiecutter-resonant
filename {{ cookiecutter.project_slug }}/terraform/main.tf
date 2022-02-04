terraform {
  required_version = ">= 1.1"

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
