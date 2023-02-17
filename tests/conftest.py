"""
Pytest Configuration File
"""

import pytest
from dotenv import load_dotenv
from typing import Any

# This needs to go above the create_app import
load_dotenv(".flaskenv")

from application import create_app


@pytest.fixture
def create_test_app() -> Any:
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
