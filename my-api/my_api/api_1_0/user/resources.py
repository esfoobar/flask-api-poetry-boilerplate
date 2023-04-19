"""
User API resources
"""

from flask import request
from flask_restx import Resource, Namespace, fields
from passlib.hash import pbkdf2_sha256

from my_api.application import db
from .models import UserModel
from .schema import UserSchema

user_ns = Namespace("users", description="User API")

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)

# Model for user post/put requests
user_post_model = user_ns.model(
    "UserPost",
    {
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "password": fields.String(required=True),
    },
)

# Model for user put requests
user_put_model = user_ns.model(
    "UserPut",
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
    },
)

# Model for user login request
user_login_model = user_ns.model(
    "UserLogin",
    {
        "username": fields.String(),
        "password": fields.String(),
    },
)


def encode_password(password):
    """Encode password with pbkdf2_sha256"""
    return pbkdf2_sha256.hash(password)


def check_email_exists(email):
    """Check if email exists"""
    return UserModel.query.filter_by(email=email).first() is not None


def check_username_exists(username):
    """Check if username exists"""
    return UserModel.query.filter_by(username=username).first() is not None


class User(Resource):
    """Individual User endpoints"""

    def get(self, user_id):
        """Get user by id"""
        user_data = UserModel.query.get(user_id)
        if user_data:
            return user_schema.dump(user_data)
        return {"message": "User not found"}, 404

    def delete(self, user_id):
        """Delete user by id"""
        user_data = UserModel.query.get(user_id)
        if user_data:
            db.session.delete(user_data)
            db.session.commit()
            return {"message": "User deleted successfully"}, 200
        return {"message": "User not found"}, 404

    @user_ns.expect(user_put_model)
    def put(self, user_id):
        """Update user by id"""
        user_data = UserModel.query.get(user_id)
        user_json = request.get_json()

        if not user_data:
            return {"message": "User not found"}, 404

        # check if username exists
        if user_json.get("username") and check_username_exists(
            user_json.get("username")
        ):
            return {"message": "Username already exists"}, 400

        # check if email exists
        if user_json.get("email") and check_email_exists(
            user_json.get("email")
        ):
            return {"message": "Email already exists"}, 400

        # validate the fields
        user_schema.validate(user_json, session=db.session, partial=True)

        # update user
        for key, value in user_json.items():
            setattr(user_data, key, value)

        db.session.commit()
        return user_schema.dump(user_data), 200


class UserList(Resource):
    """
    Endpoints for User API
    """

    @user_ns.doc("Get all the Users")
    def get(self):
        """Get all users"""
        return user_list_schema.dump(UserModel.query.all()), 200

    @user_ns.expect(user_post_model)
    @user_ns.doc("Create a User")
    def post(self):
        """Create new user"""
        user_json = request.get_json()

        # check if username exists
        if user_json.get("username") and check_username_exists(
            user_json.get("username")
        ):
            return {"message": "Username already exists"}, 400

        # check if email exists
        if user_json.get("email") and check_email_exists(
            user_json.get("email")
        ):
            return {"message": "Email already exists"}, 400

        user_data = user_schema.load(user_json, session=db.session)
        user_data.password = encode_password(user_data.password)
        db.session.add(user_data)
        db.session.commit()

        return user_schema.dump(user_data), 201


class UserLogin(Resource):
    """User login resource"""

    @user_ns.expect(user_login_model)
    @user_ns.doc("Login a User")
    def post(self):
        """Login user"""
        user_json = request.get_json()
        user_data = user_schema.load(user_json, session=db.session)

        return user_schema.dump(user_data), 201
