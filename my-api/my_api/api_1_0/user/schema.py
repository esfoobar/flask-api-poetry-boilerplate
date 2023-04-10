"""
User schema
"""

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import User


class UserSchema(SQLAlchemyAutoSchema):
    """
    User schema
    """

    class Meta:
        """
        User model class
        """

        model = User
        include_relationships = True
        load_instance = True
