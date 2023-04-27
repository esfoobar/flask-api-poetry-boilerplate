"""
User schema
"""

from marshmallow import fields, ValidationError, validates, post_load
from marshmallow_sqlalchemy import (
    SQLAlchemyAutoSchema,
)

from .models import UserModel, RoleEnum


class UserSchema(SQLAlchemyAutoSchema):
    """
    User schema
    """

    user_uid = fields.String(dump_only=True)  # read-only field
    password = fields.String(load_only=True)  # write-only field
    role_name = fields.String(required=False)

    @validates("role_name")
    def validate_role(self, value):
        """validate role value"""
        role_enum = RoleEnum.__members__.get(value.upper())
        if not role_enum:
            raise ValidationError("Invalid role value")

    @post_load
    def load_role_name(self, data, **kwargs):  # pylint: disable=unused-argument
        """load role value"""
        role_enum = RoleEnum.__members__.get(data["role_name"].upper())
        data["role"] = role_enum.value if role_enum else None
        return data

    class Meta:
        """
        User model class
        """

        model = UserModel
        include_relationships = True
        load_instance = True
        exclude = ("user_id",)  # exclude user_id from serialization
