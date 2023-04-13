"""
Api v1 namespace entrypoint
"""

from flask import Blueprint, jsonify
from flask_restx import Api
from marshmallow import ValidationError

from .user.resources import user_ns, User, UserList


api_1_0_app = Blueprint("api_1_0", __name__)


api = Api(
    api_1_0_app,
    version="1.0",
    title="Boilerplate API",
    description="Boilerplate API Platform",
    validate=True,
)


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    """Handle marshmallow validation errors"""
    return jsonify(error.messages), 400


# User resources
api.add_namespace(user_ns)
user_ns.add_resource(User, "/<int:id>")
user_ns.add_resource(UserList, "")
