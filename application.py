"""
Main Flask Application
"""

from typing import Any
from flask import Flask

from coffee.views import coffee_app


def create_app(**config_overrides: Any) -> Any:
    """
    Factory application creator
    args: config_overrides = testing overrides
    """

    app = Flask(__name__)

    # Load config
    app.config.from_pyfile("settings.py")

    # apply overrides for tests
    app.config.update(config_overrides)

    # register blueprints
    app.register_blueprint(coffee_app)

    return app
