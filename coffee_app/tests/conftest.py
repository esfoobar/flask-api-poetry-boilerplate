"""
Pytest Configuration File
"""

from typing import Any
import pytest
from dotenv import load_dotenv

# This needs to go above the create_app import
load_dotenv(".flaskenv")

# pylint: disable=wrong-import-position
# We need this file to be under the load_dotenv call
from coffee_app.application import (
    create_app,
)


@pytest.fixture(name="create_test_app")
def create_test_app_fixture() -> Any:
    """
    Creates factory app
    """
    app = create_app()
    yield app


@pytest.fixture
def create_test_client(create_test_app: Any) -> Any:
    """
    Creates test client
    """
    print("Creating test client")
    return create_test_app.test_client()
