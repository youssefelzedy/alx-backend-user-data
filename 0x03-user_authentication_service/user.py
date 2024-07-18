#!/usr/bin/env python3

'''
 User model '''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    ''' User model '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column('email', String(250), nullable=False)
    hashed_password = Column('hashed_password', String(250), nullable=False)
    session_id = Column('session_id', String(250))
    reset_token = Column('reset_token', String(250))
