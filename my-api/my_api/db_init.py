"""
Initialize database with users
"""
from passlib.hash import pbkdf2_sha256

from my_api.application import create_app, db
from my_api.api_1_0.user.models import UserModel, RoleEnum

# Create the Flask App
app = create_app()


def create_initial_users():
    """Define initial list of users"""

    users = [
        {
            "username": "admin",
            "email": "admin@example.com",
            "password": "12345",
            "role": RoleEnum.ADMIN.value,
        },
        {
            "username": "user1",
            "email": "user1@example.com",
            "password": "12345",
            "role": RoleEnum.USER.value,
        },
    ]

    # Create tables
    db.create_all()

    # Populate users
    for user in users:
        if not UserModel.query.filter_by(username=user["username"]).first():
            new_user = UserModel(
                username=user["username"],
                email=user["email"],
                password=pbkdf2_sha256.hash(user["password"]),
                role=user["role"],
            )
            db.session.add(new_user)
        db.session.commit()


# Run the script
if __name__ == "__main__":
    with app.app_context():
        create_initial_users()
