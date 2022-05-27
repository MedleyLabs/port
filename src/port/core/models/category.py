from datetime import datetime

from ..port import db, ma
from ..port.core.models import BaseModel


class Category(BaseModel):
    """ """
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow)

    @classmethod
    def seed(cls, fake):
        """class utility to create fake accounts to see the db"""
        category = Category(
            name=fake.state()
        )
        category.save()


class CategorySchema(ma.ModelSchema):
    """Define marshmallow schema"""
    class Meta:
        model = Category

