"""
User model
"""
from my_api.application import db


# mypy: ignore-errors
class User(db.Model):
    """
    User model
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
