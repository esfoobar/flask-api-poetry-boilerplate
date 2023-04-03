"""
Pytest Configuration File
"""

from typing import Any
import pytest

from my_app.application import (
    create_app,
)


@pytest.fixture(name="create_test_app")
def create_test_app_fixture() -> Any:
    """
    Creates factory app
    """
    app = create_app(ENV_FOR_DYNACONF="testing")
    yield app


@pytest.fixture
def create_test_client(create_test_app: Any) -> Any:
    """
    Creates test client
    """
    print("Creating test client")
    return create_test_app.test_client()
