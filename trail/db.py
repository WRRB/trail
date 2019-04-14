from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///:memory:')
session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine))()

Base = declarative_base()


def add_all(records):
    session.add_all(records)
    session.commit()


def find_all(entity):
    return session.query(entity).all()
