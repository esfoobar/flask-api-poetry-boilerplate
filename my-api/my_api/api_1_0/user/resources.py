"""
User API resources
"""

from typing import Any, Tuple
from flask_restx import Resource, Namespace
from marshmallow.exceptions import ValidationError

from my_api.application import db
from .schema import UserSchema

api = Namespace("user", description="User API")


@api.route("/")
class UserResource(Resource):  # type: ignore
    """
    Endpoints for User API
    """

    def post(self) -> Tuple[dict[str, Any], int]:
        """Create new user"""

        user_schema = UserSchema()  # type: ignore
        try:
            result = user_schema.load(api.payload, session=db.session)  # type: ignore
        except ValidationError as err:
            request_error = {
                "errors": err.messages,
                "message": "VALIDATION_ERROR",
            }
            return request_error, 400
        message = "User created"
        print(result)
        return {"message": message}, 201
