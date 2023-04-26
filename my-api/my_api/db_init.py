"""
Initialize database with users
"""

from flask import current_app
from my_api.api_1_0.user.models import UserModel, RoleEnum
from .application import db

# Define initial list of users
users = [
    {
        "username": "admin",
        "email": "admin@example.com",
        "password": "12345",
        "role": RoleEnum.ADMIN,
    },
    {
        "username": "user1",
        "email": "user1@example.com",
        "password": "12345",
        "role": RoleEnum.USER,
    },
]

# Create tables
with current_app.app_context():
    db.create_all()

# Populate users
for user in users:
    if not UserModel.query.filter_by(username=user["username"]).first():
        new_user = UserModel(
            username=user["username"],
            email=user["email"],
            password=user["password"],
            role=user["role"],
        )
        db.session.add(new_user)
    db.session.commit()
