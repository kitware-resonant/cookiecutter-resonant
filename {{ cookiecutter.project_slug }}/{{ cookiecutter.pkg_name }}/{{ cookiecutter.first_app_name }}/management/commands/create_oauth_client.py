from allauth.idp.oidc.models import Client
import djclick as click

REDIRECT_URI = 'http://localhost:1234/'


@click.command()
def create_oauth_client():
    client, created = Client.objects.get_or_create(
        name='resonant-oauth-client-example',
        # From 
        # https://github.com/kitware-resonant/resonant-oauth-client/blob/master/example/index.js#L5
        id='Qir0Aq7AKIsAkMDLQe9MEfORbHEBKsViNhAKJf1A',
        defaults=dict(
            scopes='openid',
            type=Client.Type.PUBLIC,
            grant_types=Client.GrantType.AUTHORIZATION_CODE,
            redirect_uris=REDIRECT_URI,
            response_types='code',
            skip_consent=False,
        ),
    )

    if created:
        click.echo(f'Created new OAuth client: {client.name} with ID: {client.id}')
    else:
        click.echo(f'OAuth client already exists: {client.name} with ID: {client.id}')
