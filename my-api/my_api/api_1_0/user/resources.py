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

# Model for user post/put requests
user_req_model = user_ns.model(
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
        user_data = UserModel.query.filter_by(id=id).first()
        if user_data:
            return user_schema.dump(user_data)
        return {"message": "User not found"}, 404

    def delete(self, id):
        """Delete user by id"""
        user_data = UserModel.query.filter_by(id=id)
        if user_data:
            user_data.delete()
            db.session.commit()
            return {"message": "User deleted successfully"}, 200
        return {"message": "User not found"}, 404

    @user_ns.expect(user_req_model)
    def put(self, id):
        """Update user by id"""
        user_data = UserModel.query.filter_by(id=id).first()
        user_json = request.get_json()

        if not user_data:
            return {"message": "User not found"}, 404

        # update user
        user_update_data = user_schema.load(user_json, session=db.session)
        user_data.username = user_update_data.username
        user_data.email = user_update_data.email

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

    @user_ns.expect(user_req_model)
    @user_ns.doc("Create a User")
    def post(self):
        """Create new user"""
        user_json = request.get_json()
        user_data = user_schema.load(user_json, session=db.session)
        db.session.add(user_data)
        db.session.commit()

        return user_schema.dump(user_data), 201
