"""
Pytest Configuration File
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, drop_database, database_exists
from dynaconf import settings

from my_api.application import create_app, db


@pytest.fixture
def create_db():
    """
    Create sqlalchemy connection and test datatabase
    """
    print("Creating db")

    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")

    db_test_uri = settings.SQLALCHEMY_TEST_DATABASE_URI

    # drop the database if it exists
    if database_exists(db_test_uri):
        drop_database(db_test_uri)

    # create test database
    create_database(db_test_uri)

    yield {}

    print("Destroying db")

    # create new engine to drop test database
    drop_database(db_test_uri)


@pytest.fixture
def create_test_app(create_db):
    """
    Create a test factory app
    """
    app = create_app(**create_db)
    app_context = app.app_context()
    app_context.push()
    db.create_all()
    yield app
    db.session.remove()
    db.drop_all()


@pytest.fixture
def create_test_client(create_test_app):
    """
    Create a test client
    """
    print("Creating test client")
    return create_test_app.test_client()
