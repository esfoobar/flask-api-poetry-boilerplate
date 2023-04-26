"""
User API resources
"""

from flask import jsonify, request
from flask_restx import Resource, Namespace, fields, reqparse
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
)

from my_api.application import db
from my_api.api_1_0.utils import paginate_metadata_object
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

# pagination params
parser = reqparse.RequestParser()
parser.add_argument(
    "users_per_page",
    type=int,
    help="Number of users per page",
    default=10,
    required=False,
)
parser.add_argument(
    "page",
    type=int,
    help="Current page",
    default=1,
    required=False,
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

    def get(self, user_uuid):
        """Get user by id"""
        user_data = UserModel.query.filter_by(user_uuid=user_uuid).first()
        if user_data:
            return user_schema.dump(user_data)
        return {"message": "User not found"}, 404

    def delete(self, user_uuid):
        """Delete user by id"""
        user_data = UserModel.query.filter_by(user_uuid=user_uuid).first()
        if user_data:
            db.session.delete(user_data)
            db.session.commit()
            return {"message": "User deleted successfully"}, 200
        return {"message": "User not found"}, 404

    @user_ns.expect(user_put_model)
    def put(self, user_uuid):
        """Update user by id"""
        user_data = UserModel.query.filter_by(user_uuid=user_uuid).first()
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

    @user_ns.expect(parser)
    def get(self):
        """Get all users"""
        args = parser.parse_args()
        user_list = UserModel.query.paginate(
            page=args.page, per_page=args.users_per_page
        )

        return {
            "_meta": paginate_metadata_object(user_list),
            "users": user_list_schema.dump(user_list),
        }, 200

    @user_ns.expect(user_post_model)
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
    def post(self):
        """Login user"""
        user_json = request.get_json()

        # Flask RestX won't handle missing data if there's no marshmallow load
        # So we need to check for missing data manually
        if not user_json.get("username"):
            return {"message": "Missing username parameter"}, 400
        if not user_json.get("password"):
            return {"message": "Missing password parameter"}, 400

        # check if user exists in database
        user = UserModel.query.filter_by(username=user_json["username"]).first()
        if not user:
            return {"message": "Invalid credentials"}, 401

        # check if password is correct
        if not pbkdf2_sha256.verify(user_json["password"], user.password):
            return {"message": "Invalid credentials"}, 401

        # create jwt access token
        access_token = create_access_token(identity=user.email, fresh=True)
        refresh_token = create_refresh_token(identity=user.email)

        response = jsonify(
            {
                "id": user.user_id,
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        )

        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        response.status_code = 200
        return response
