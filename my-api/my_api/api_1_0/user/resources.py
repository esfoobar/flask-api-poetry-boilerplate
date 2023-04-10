"""
User API resources
"""

from flask_restplus import Resource, Namespace, abort, fields

api = Namespace("user", description="User API")


@api.route("/")
class UsersEndpoint(Resource):
    """
    Endpoints for User API
    """

    def post(self):
        """Create new user"""
