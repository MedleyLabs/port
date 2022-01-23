from . import db
from datetime import datetime


class Shortcut(db.Model):
    """ Each instance represnts the plant being watered """
    __tablename__ = 'shortcut'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    download_url = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    is_active = db.Columnn(db.Boolean, nullable=False)


class ShortcutDependencies(db.Model):
    """ Sets the dependency chain for shortcut downloads """
    __tablename__ = 'shortcut_dependencies'

    id = db.Column(db.Integer, primary_key=True)
    parent = db.ForeignKey('shortcut.id', nullable=False)
    child = db.ForeignKey('shortcut.id', nullable=False)
