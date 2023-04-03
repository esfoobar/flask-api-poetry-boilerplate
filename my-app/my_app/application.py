"""
Main Flask Application
"""

from typing import Any
from flask import Flask
from dynaconf import FlaskDynaconf


from my_app.home_app.views import home_app


def create_app(**config_overrides: Any) -> Any:
    """
    Factory application creator
    args: config_overrides = testing overrides
    """

    app = Flask(__name__)

    # Load config
    FlaskDynaconf(app, **config_overrides)

    # apply overrides for tests
    app.config.update(config_overrides)

    # register blueprints
    app.register_blueprint(home_app)

    return app
