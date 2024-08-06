data "aws_route53_zone" "this" {
  # This must be created by hand in the AWS console
  name = "{{ cookiecutter.site_domain.split('.', 1)[1] }}"
}

data "heroku_team" "this" {
  name = "kitware"
}

module "django" {
  source  = "girder/girder4/heroku"
  version = "0.13.0"

  project_slug     = "{{ cookiecutter.project_slug }}"
  route53_zone_id  = data.aws_route53_zone.this.zone_id
  heroku_team_name = data.heroku_team.this.name
  subdomain_name   = "{{ cookiecutter.site_domain.split('.', 1)[0] }}"
}
