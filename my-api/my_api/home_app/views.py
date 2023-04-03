"""
home application. Flask uses the MTV (Model, Template, Views) architecture 
instead of MVC (Model, View, Controller). 
To learn more visit: https://flask.palletsprojects.com/en/2.2.x/
"""

from flask import Blueprint, current_app

# This defines a "home_app" Blueprint for how to construct or extend the main application.
# To learn more go to: https://flask.palletsprojects.com/en/2.2.x/blueprints/
home_app = Blueprint("home_app", __name__)


@home_app.route("/")
def home() -> str:
    """
    The home page for a home type
    """

    return (
        "<h3>Home: Hello World!</h3>"
        + f"<p>Dynaconf Environment: {current_app.config.ENV_FOR_DYNACONF}</br>"  # type: ignore
        + f"DATABASE_NAME: {current_app.config.DATABASE_NAME}</p>"  # type: ignore
    )
