"""
Main Flask Application
"""

from typing import Any
from flask import Flask
from dynaconf import FlaskDynaconf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from my_api.home_app.views import home_app

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

    # register blueprints
    app.register_blueprint(home_app)

    return app
