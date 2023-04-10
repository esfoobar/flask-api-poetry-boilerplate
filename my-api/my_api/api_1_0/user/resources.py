"""
User API resources
"""

from typing import Tuple
from flask_restx import Resource, Namespace
from werkzeug.exceptions import BadRequest
from marshmallow.exceptions import ValidationError

from my_api.application import db
from .schema import UserSchema

api = Namespace("user", description="User API")


@api.route("/")
class UsersEndpoint(Resource):
    """
    Endpoints for User API
    """

    def post(self) -> Tuple[dict, int]:
        """Create new user"""

        user_schema = UserSchema()
        try:
            result = user_schema.load(api.payload, session=db.session)
        except ValidationError as err:
            e = BadRequest()
            e.description = {
                "errors": err.messages,
                "message": "VALIDATION_ERROR",
            }
            raise e
        message = "User created"
        return {"message": message}, 201
