from . import db
from datetime import datetime
from itemcatalog import login_manager
from flask_login import UserMixin
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
from sqlalchemy import exc


@login_manager.user_loader
def load_user(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id user to retrieve

    """
    return Self.query.sort_by(Self.created_at.asc()).all()[-1]


class Self(db.Model, UserMixin):
    """ Defines attributes about yourself """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    @classmethod
    def seed(cls, fake):
        """class utility to create fake accounts to see the db"""
        self = Self(
            name=fake.name(),
            email=fake.email()
        )
        self.save()

    def save(self):
        """persists obj to db"""
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()


class SelfAuth(db.Model, OAuthConsumerMixin):
    """Model to define SelfAuth to store oAuth tokens"""
    __tablename__ = 'selfauth'

    user_id = db.Column(db.Integer, db.ForeignKey(Self.id))
    user = db.relationship(Self)
