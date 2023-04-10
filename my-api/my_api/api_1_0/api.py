"""
Api v1 namespace entrypoint
"""

from flask import Blueprint
from flask_restplus import Api

api_1_0_app = Blueprint("api_1_0", __name__)

from api_1_0.user.resources import api as user_ns

authorizations = {
    "apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}
}

api = Api(
    api_1_0_app,
    version="1.0",
    title="Boilerplate API",
    description="Boilerplate API Platform",
    validate=True,
    authorizations=authorizations,
)

api.add_namespace(ns=user_ns, path="/users")
