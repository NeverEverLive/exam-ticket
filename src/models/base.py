from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_mixins import AllFeaturesMixin
from settings.config import settings

import logging

Base = declarative_base()


class BaseModel(Base, AllFeaturesMixin):
    """Postgres base model"""
    __abstract__ = True
    pass


def get_session():
    """Получить текущую сессию"""
    engine = create_engine(settings.get_db_url())
    return Session(engine)


def set_session():
    """Создать сессию"""

    logging.warning(settings.get_db_url())
    print(settings.get_db_url())

    engine = create_engine(settings.get_db_url())
    db_session = scoped_session(
        sessionmaker(autocommit=True, autoflush=True, bind=engine)
    )
    BaseModel.set_session(db_session)
    Base.query = db_session.query_property()
    Base.metadata.create_all(engine)


# def drop_all():
#     engine = create_engine(PGStorageSettings().geturl())
#     Base.metadata.drop_all(engine)
