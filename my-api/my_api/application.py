"""
Main Flask Application
"""

from datetime import timedelta
from typing import Any
from flask import Flask
from dynaconf import FlaskDynaconf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

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

    # setup CORS
    CORS(
        app,
        resources={
            r"/v1.0/*": {
                "origins": app.config["CORS_ORIGINS"],
                "allow_headers": [
                    "Content-Type",
                    "Authorization",
                    "Access-Control-Allow-Credentials",
                    "X-CSRF-TOKEN",
                ],
            }
        },
        supports_credentials=True,
    )

    # setup JWT
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    jwt = JWTManager(app)  # pylint: disable=unused-variable

    # initialize db
    db.init_app(app)
    Migrate(app, db)

    # import blueprints
    from my_api.api_1_0.api import api_1_0_app

    # register blueprints
    app.register_blueprint(api_1_0_app, url_prefix="/v1.0")

    return app
