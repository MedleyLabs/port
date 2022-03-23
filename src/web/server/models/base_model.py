from sqlalchemy import exc

from . import db


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        """ Persists obj to db. """
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()

    def to_dict(self):
        """ Return a dictionary representation of this model. """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
