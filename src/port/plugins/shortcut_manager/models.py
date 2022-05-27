from port import db
from port.core.models import BaseModel


class Shortcut(BaseModel):
    """ Each instance represnts the plant being watered """
    __tablename__ = 'shortcut'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    download_url = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)


class ShortcutDependencies(BaseModel):
    """ Sets the dependency chain for shortcut downloads """
    __tablename__ = 'shortcut_dependencies'

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.ForeignKey('shortcut.id', nullable=False)
    child_id = db.ForeignKey('shortcut.id', nullable=False)
