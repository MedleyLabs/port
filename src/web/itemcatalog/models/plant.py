from . import db, ma
from datetime import datetime


class Plant(db.Model):
    """ An instance is a single plant that you take care of. """
    __tablename__ = 'plant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
    days_between_water = db.Column(db.Integer, nullable=False)
    days_between_fertilizer = db.Column(db.Integer, nullable=False)
    days_between_repot = db.Column(db.Integer, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class PlantSchema(ma.ModelSchema):
    """Define marshmallow schema"""
    class Meta:
        model = Plant


class WaterEntry(db.Model):
    """ Each instance represnts the plant being watered """
    __tablename__ = 'water_entry'

    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    amount = db.Column(db.Float())


class WaterEntrySchema(ma.ModelSchema):
    """Define marshmallow schema"""
    class Meta:
        model = WaterEntry
