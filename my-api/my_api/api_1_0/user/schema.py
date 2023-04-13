"""
User schema
"""

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import UserModel


class UserSchema(SQLAlchemyAutoSchema):
    """
    User schema
    """

    class Meta:
        """
        User model class
        """

        model = UserModel
        include_relationships = True
        load_instance = True
