from flask_login import UserMixin
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from port import db, login_manager
from port.models import BaseModel


@login_manager.user_loader
def load_user(user_id):
    """Given *user_id*, return the associated User object.
    :param unicode user_id: user_id user to retrieve
    """
    return User.query.get(int(user_id))


class User(BaseModel, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def set_password(self, password):
        """ Hashes the password and stores it """
        self.password = generate_password_hash(password, method='sha256')

    def validate_password(self, password):
        """ Check that the provided password matches the hashed password """
        return check_password_hash(self.password, password)


class UserAuth(BaseModel, OAuthConsumerMixin):
    """Model to define UserAuth to store oAuth tokens"""
    __tablename__ = 'userauth'

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
