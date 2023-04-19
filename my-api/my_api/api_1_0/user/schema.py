"""
User schema
"""

from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import UserModel


class UserSchema(SQLAlchemyAutoSchema):
    """
    User schema
    """

    password = fields.String(load_only=True)

    class Meta:
        """
        User model class
        """

        model = UserModel
        include_relationships = True
        load_instance = True
