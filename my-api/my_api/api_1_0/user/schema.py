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

    user_uid = fields.String(dump_only=True)  # read-only field
    password = fields.String(load_only=True)  # write-only field

    class Meta:
        """
        User model class
        """

        model = UserModel
        include_relationships = True
        load_instance = True
        exclude = ("user_id",)  # exclude user_id from serialization
