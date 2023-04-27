"""
Api v1 namespace entrypoint
"""

from flask import Blueprint
from flask_restx import Api

from .user.resources import user_ns, User, UserList, UserLogin


api_1_0_app = Blueprint("api_1_0", __name__)


api = Api(
    api_1_0_app,
    version="1.0",
    title="Boilerplate API",
    description="Boilerplate API Platform",
    validate=True,
)

# User resources
api.add_namespace(user_ns)
user_ns.add_resource(User, "/<string:user_uuid>")
user_ns.add_resource(UserList, "")
user_ns.add_resource(UserLogin, "/login")
