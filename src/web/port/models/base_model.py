from port import db
from sqlalchemy import exc


class BaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def all(cls, to_dict=True, include_instance_state=False):
        models = cls.query.all()
        if to_dict:
            models = [model.to_dict(include_instance_state=include_instance_state) for model in models]
        return models

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    @property
    def schema_name(self):
        """ The name of the database schema is the same as the plugin name """
        plugin_name = self.__module__.split('.')[0]
        return plugin_name

    def save(self):
        """ Persists obj to db. """
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()

    def to_dict(self, include_instance_state=True):
        """ Return a dictionary representation of this model. """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns
                if include_instance_state or c.name != '_sa_instance_state'}
