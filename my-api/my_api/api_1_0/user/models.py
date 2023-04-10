"""
User model
"""
from my_api.application import db


class User(db.Model):  # type: ignore
    # Flask-SqlAlchemy still has no type hints
    """
    User model
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
