#!/usr/bin/env python3

'''
Main file
'''

from auth import Auth
from flask import (Flask,
                   jsonify,
                   request,
                   abort,
                   redirect)

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome() -> str:
    '''GET /
    Return: welcome message
    '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register() -> str:
    '''POST /users
    Return: JSON payload
    '''
    try:
        email = request.form.get('email')
        password = request.form.get('password')
    except KeyError:
        abort(400)

    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    '''POST /sessions
    Return: JSON payload
    '''
    try:
        email = request.form.get('email')
        password = request.form.get('password')
    except KeyError:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    if not session_id:
        abort(401)
        
    msg = {"email": email, "message": "logged in"}
    response = jsonify(msg)

    response.set_cookie("session_id", session_id)
    
    return response



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
