#!/usr/bin/env python3
'''
Auth module
'''

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from user import User


def _hash_password(password: str) -> bytes:
    '''Hash a password
    '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
