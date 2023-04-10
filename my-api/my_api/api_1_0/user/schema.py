"""
User schema
"""

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from my_api.api_1_0.user.models import User


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
