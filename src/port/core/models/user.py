from datetime import datetime
from flask_login import UserMixin
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin

from ... import db, login_manager
from ...core.models import BaseModel


@login_manager.user_loader
def load_user(user_id):
    """Given *user_id*, return the associated User object.
    :param unicode user_id: user_id user to retrieve
    """
    return User.query.get(int(user_id))


class User(BaseModel, UserMixin):
    """ A user """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    is_primary = db.Column()
    time_inserted = db.Column(db.DateTime(), default=datetime.utcnow)
    time_updated = db.Column(db.DateTime(), default=datetime.utcnow)


class UserAuth(BaseModel, OAuthConsumerMixin):
    """Model to define UserAuth to store oAuth tokens"""
    __tablename__ = 'userauth'

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
