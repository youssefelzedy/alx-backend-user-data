#!/usr/bin/env python3
"""
Session Authentication
"""

from typing import Dict
from api.v1.auth.auth import Auth
from datetime import datetime
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session Authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''Create a session ID
        '''

        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        Returns a User ID based on a Session ID
        '''

        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        '''
        Returns a User instance based on a cookie value
        '''

        cookie = self.session_cookie(request)
        session_user_id = self.user_id_for_session_id(cookie)
        usr_id = User.get(session_user_id)
        return usr_id
