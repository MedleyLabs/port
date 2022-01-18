from . import db, ma
from datetime import datetime


class Plant(db.Model):
    """ An instance is a single plant that you take care of. """
    __tablename__ = 'plant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
    days_between_water = db.Column(db.Integer, nullable=False)
    days_between_fertilizer = db.Column(db.Integer, nullable=False)
    days_between_repot = db.Column(db.Integer, nullable=False)


class PlantSchema(ma.ModelSchema):
    """Define marshmallow schema"""
    class Meta:
        model = Plant
