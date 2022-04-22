"""
Create session DB
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


db_string = settings.SQLALCHEMY_DATABASE_URI

engine = create_engine(db_string, connect_args={'check_same_thread': False})
base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
