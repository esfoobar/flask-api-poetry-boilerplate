"""
Main Flask Application
"""

from typing import Any
from flask import Flask
from dynaconf import FlaskDynaconf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from my_api.api_1_0.api import home_app

# setup db
db = SQLAlchemy()


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

    # initialize db
    db.init_app(app)
    Migrate(app, db)

    # import blueprints
    from api_1_0.api import api_1_0_app

    # register blueprints
    app.register_blueprint(api_1_0_app, url_prefix="/v1.0")

    return app
