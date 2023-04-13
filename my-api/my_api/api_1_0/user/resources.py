"""
User API resources
"""

from flask import request
from flask_restx import Resource, Namespace, fields

from my_api.application import db
from .models import UserModel
from .schema import UserSchema

user_ns = Namespace("user", description="User API")

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)

# Model for user post
user_model = user_ns.model(
    "User",
    {
        "username": fields.String(required=True),
        "email": fields.String(required=True),
    },
)


class User(Resource):
    """Individual User endpoints"""

    def get(self, id):
        """Get user by id"""
        user_data = UserModel.find_by_id(id)
        if user_data:
            return user_schema.dump(user_data)
        return {"message": "User not found"}, 404


class UserList(Resource):
    """
    Endpoints for User API
    """

    @user_ns.expect(user_model)
    def post(self):
        """Create new user"""
        user_json = request.get_json()
        user_data = user_schema.load(user_json, session=db.session)
        user_data.save_to_db()

        return user_schema.dump(user_data), 201
