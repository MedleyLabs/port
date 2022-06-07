from flask import Blueprint, redirect, url_for, session, flash
from flask_login import current_user, login_user, logout_user


auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():
    """ Login an authorized user """
    pass


@auth.route('/logout')
def logout():
    """ Logs out an authorized user """
    pass