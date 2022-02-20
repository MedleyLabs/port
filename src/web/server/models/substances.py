from . import db
from .base_model import BaseModel


class Entry(BaseModel):
    """ An instance is a single plant that you take care of. """
    __tablename__ = 'plant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), nullable=False)
    dose_quantity = db.Column(db.Float)
    dose_units = db.Column(db.String(128), nullable=False)
