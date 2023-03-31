"""
Home App Tests
"""


from typing import Any


def test_initial_response(
    create_test_client: Any, create_test_app: Any
) -> None:
    """
    Test app's response
    """
    response = create_test_client.get("/")
    body = response.get_data()
    assert "Hello World!" in str(body)
    assert create_test_app.config.DB_HOST == "testing-db"
