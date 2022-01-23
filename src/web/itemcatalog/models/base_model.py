from . import db


class BaseModel(db.Model):
    __abstract__ = True

    def to_dict(self):
        """Return a dictionary representation of this model."""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
