"""
User model
"""
import uuid
import enum
from sqlalchemy import event

from my_api.application import db


class RoleEnum(enum.Enum):
    """
    User roles
    """

    ADMIN = 0
    USER = 1


class UserModel(db.Model):

    """
    User model
    """

    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    user_uuid = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.Integer, nullable=False, default=RoleEnum.USER.value)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<User {UserModel.username}>"


def generate_uuid(mapper, connection, target):
    """generate uuid"""
    target.user_uuid = str(uuid.uuid4())


event.listen(UserModel, "before_insert", generate_uuid, propagate=True)
