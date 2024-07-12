#!/usr/bin/env python3

'''
This module is responsible for
checking if the session token has expired or not.
'''

from os import getenv
from datetime import datetime, timedelta, timezone
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    '''
    Session expiration Authentication
    '''

    def __init__(self):
        '''
        Constructor
        '''

        try:
            session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            session_duration = 0
        self.session_duration = session_duration

    def create_session(self, user_id=None):
        '''
        Creates a Session ID for a user_id
        '''
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dict = {'user_id': user_id, 'created_at': datetime.now()}
        SessionAuth.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        '''
        Returns a User ID based on a Session ID
        '''

        if session_id is None:
            return None
        if session_id not in SessionAuth.user_id_by_session_id.keys():
            return None

        session_dict = SessionAuth.user_id_by_session_id[session_id]

        if self.session_duration <= 0:
            return session_dict.get('user_id')
        if 'created_at' not in session_dict.keys():
            return None
        if (timedelta(seconds=self.session_duration) +
                session_dict.get('created_at')) < datetime.now():
            return None
        return session_dict.get('user_id')
