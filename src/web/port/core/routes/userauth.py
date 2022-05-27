from flask import Blueprint, redirect, url_for, session, flash
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_login import current_user, login_user, logout_user
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound
from oauthlib.oauth2.rfc6749.errors import InvalidClientIdError


userauth = Blueprint('userauth', __name__)


@userauth.route("/login")
def login():
    """ Login an authorized user """
    pass


@userauth.route('/logout')
def logout():
    """ Logs out an authorized user """
    pass