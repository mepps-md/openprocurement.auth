# coding: utf-8
from openprocurement.auth.provider_app import oauth_provider
from redis import Redis
import openprocurement.auth.models
import openprocurement.auth.views


def make_oath_provider_app(
        global_conf,
        redis='redis://localhost:9002/1',
        secret='abcdfg',
        timezone='Europe/Kiev',
        hash_secret_key='',
        auction_client_id='',
        auction_client_secret=''):

    oauth_provider.debug = True
    oauth_provider.db = Redis.from_url(redis)
    oauth_provider.secret_key = secret
    oauth_provider.hash_secret_key = hash_secret_key
    oauth_provider.config['OAUTH2_PROVIDER_TOKEN_EXPIRES_IN'] = openprocurement.auth.models.GRANT_EXPIRES

    oauth_provider.auction_client = openprocurement.auth.models.Client(
        client_id=auction_client_id,
        client_secret=auction_client_secret,
        _redirect_uris=' '.join(
            ['http:\/\/localhost:.*',
             '(http|https):\/\/[\w\-_]+\.office\.quintagroup\.com.*',
             '(http|https):\/\/[.\w\-_]+\.openprocurement\.org\.*']
        ),
        _default_scopes='email'
    )

    return oauth_provider
