from flask import Blueprint, redirect, url_for, session, flash, make_response, request
from flask_login import current_user, login_user, logout_user

from port import login_manager
from port.models import User


auth = Blueprint('auth', __name__)


@auth.route('/auth/login', methods=['POST'])
def login():
    """ Authorize and login a user """

    print('Running /api/login...')

    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user:
        message = f'User with user.name={user.name} does not exist!'
        print(message)
        return make_response(message, 400)

    if user.validate_password(password):
        print(f'Logging in user with user.name={user.name}...')
        login_user(user, remember=True)
        return 200

    message = f'Invalid password for alias={alias}!'
    logger.info(message)
    return make_response(message, 400)


@auth.route('/logout')
def logout():
    """ Logs out an authorized user """
    pass


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
