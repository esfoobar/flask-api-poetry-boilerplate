"""
Coffee application. 
"""

from flask import Blueprint

# This defines a "coffee_app" Blueprint for how to construct or extend the main application.
# To learn more go to: https://flask.palletsprojects.com/en/2.2.x/blueprints/ 
coffee_app = Blueprint("coffee_app", __name__)


@coffee_app.route("/")
def home() -> str:
    """
    The home page for a coffee type
    """

    return "<h3>Home: Hello World!</h3>"
