#!/usr/bin/env python3
""" Module for session authentication views
"""

from werkzeug import exceptions
from flask import request, jsonify, abort
from api.v1.views import app_views
from models.user import User
from api.v1.auth.session_auth import SessionAuth
from os import abort, environ, getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - User object JSON represented
    """
    email = request.form.get("email", None)
    password = request.form.get("password", None)

    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    cookie_response = getenv('SESSION_NAME')
    response = jsonify(user[0].to_json())
    response.set_cookie(cookie_response, session_id)
    return response
