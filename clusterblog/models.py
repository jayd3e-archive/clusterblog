from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base


class BaseClass(object):
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=BaseClass)


def initialize_base(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)


class Post(Base):
    __tablename__ = 'posts'

    title = Column(String(50))
    body = Column(String(2000))
    date = Column(Date)
    created = Column(DateTime)
    change_time = Column(DateTime)

    def __repr__(self):
        return "<Post('%s')>" % (self.id)


class User(Base):
    __tablename__ = 'users'

    # Main Fields
    username = Column(String(15))
    email = Column(String(50))
    joined = Column(DateTime)
    last_online = Column(DateTime)

    def __repr__(self):
        return "<User('%s')>" % (self.id)
