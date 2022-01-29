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
    days_between_fertilize = db.Column(db.Integer, nullable=False)
    days_between_repot = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)


class FertilizeEntry(BaseModel):
    """ Tracks when each plant is fertilized """
    __tablename__ = 'fertilize_entry'

    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)


class RepotEntry(BaseModel):
    """ Tracks when each plant is repotted """
    __tablename__ = 'repot_entry'

    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)


class WaterEntry(BaseModel):
    """ Tracks when each plant is watered """
    __tablename__ = 'water_entry'

    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    chosen_date = db.Column(db.DateTime(), nullable=False)
    entry_type = db.Column(db.String(32), nullable=False)
    entry_value = db.Column(db.Float)
