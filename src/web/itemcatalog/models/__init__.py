from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from itemcatalog import app


__all__ = ["db", "ma"]

db = SQLAlchemy(app)
ma = Marshmallow(app)
