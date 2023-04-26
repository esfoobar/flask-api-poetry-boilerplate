"""
User model
"""
from my_api.application import db


class UserModel(db.Model):

    """
    User model
    """

    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    user_uuid = db.Column(
        db.String,
        unique=True,
        nullable=False,
        default=db.func.uuid_generate_v4(),
    )
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
