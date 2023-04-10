"""
User API resources
"""

from flask import Response
from flask_restx import Resource, Namespace
from werkzeug.exceptions import BadRequest
from marshmallow.exceptions import ValidationError

from .schema import UserSchema
from my_api.application import db

api = Namespace("user", description="User API")


@api.route("/")
class UsersEndpoint(Resource):
    """
    Endpoints for User API
    """

    def post(self) -> Response:
        """Create new user"""

        user_schema = UserSchema()
        try:
            result = user_schema.load(api.payload, session=db.session)
        except ValidationError as err:
            e = BadRequest()
            e.data = {"errors": err.messages, "message": "VALIDATION_ERROR"}
            raise e
        message = "User created"
        return {"message": message}, 201
