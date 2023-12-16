from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

Engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = declarative_base()

def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()