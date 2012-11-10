from pyramid.security import unauthenticated_userid
from clusterblog.models import User


def get_db(request):
    maker = request.registry.settings['db.sessionmaker']
    return maker()


def get_user(request):
    db = request.db
    user_id = unauthenticated_userid(request)
    if user_id is not None:
        # this should return None if the user doesn't exist
        # in the database
        return db.query(User).filter_by(id=user_id).first()
    return None
