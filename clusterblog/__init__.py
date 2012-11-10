from pyramid.config import Configurator
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

from clusterblog.request import (
    get_db,
    get_user
)
from clusterblog.resources import Site
from clusterblog.models import (
    Post,
    User,
    initialize_base
)
from clusterblog.security import groupfinder


def main(global_config, **settings):
    '''Main config function'''

    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_base(engine)
    maker = sessionmaker(bind=engine, extension=ZopeTransactionExtension())
    settings['db.sessionmaker'] = maker

    authentication_policy = SessionAuthenticationPolicy(callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings,
                          root_factory=Site,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy)

    # Sessions
    config.include('pyramid_redis_sessions')

    # Request
    config.set_request_property(get_db, 'db', reify=True)
    config.set_request_property(get_user, 'user', reify=True)

    # Route Configuration
    config.add_route('index', '/')

    # Post
    config.add_route('posts', '/posts')
    config.add_route('post', '/post')

    config.scan('clusterblog.views')
    return config.make_wsgi_app()
