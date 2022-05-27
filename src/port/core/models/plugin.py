from datetime import datetime

from src.port import db, ma
from src.port.core.models import BaseModel


class Plugin(BaseModel):
    """ Define a plugin that extends port functionality """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)


class PluginVersion(BaseModel):
    """ Define the particular version of a plugin """

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)


class PluginSchema(ma.ModelSchema):
    """Define marshmallow schema"""
    class Meta:
        model = Plugin
