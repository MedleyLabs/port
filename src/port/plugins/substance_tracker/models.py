from port import db
from port.core.models import BaseModel


class Entry(BaseModel):
    """ An entry documents the use of a single substance at one time.. """
    __tablename__ = 'entry'

    id = db.Column(db.Integer, primary_key=True)
    substance_id = db.Column(db.Integer, nullable=False, unique=True)
    amount = db.Column(db.Float)
    created_at = db.Column(db.DateTime(), nullable=False)


class Substance(BaseModel):
    """ A substance could be anything that you want to track consumption. """
    __tablename__ = 'substance'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    route_id = db.Column(db.ForeignKey('substance_route.id'))


class SubstanceRoute(BaseModel):
    """ A route is a how the substance is used (ingested, smoked, ...) """
    __tablename__ = 'substance_route'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    units = db.Column(db.String, nullable=False)
