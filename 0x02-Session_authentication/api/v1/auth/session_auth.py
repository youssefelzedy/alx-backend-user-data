#!/usr/bin/env python3
"""
Session Authentication
"""

from typing import Dict
from api.v1.auth.auth import Auth
from datetime import datetime
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