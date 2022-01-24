from . import db, ma
from .base_model import BaseModel


class Plant(BaseModel):
    """ An instance is a single plant that you take care of. """
    __tablename__ = 'plant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime())
    days_between_water = db.Column(db.Integer, nullable=False)
    days_between_fertilizer = db.Column(db.Integer, nullable=False)
    days_between_repot = db.Column(db.Integer, nullable=False)


class Entry(BaseModel):
    """ Generic class for logging a plant care entry """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)


class FertilizeEntry(Entry):
    """ Tracks when each plant is fertilized """
    __tablename__ = 'fertilize_entry'


class RepotEntry(Entry):
    """ Tracks when each plant is repotted """
    __tablename__ = 'repot_entry'


class WaterEntry(Entry):
    """ Tracks when each plant is watered """
    __tablename__ = 'water_entry'
