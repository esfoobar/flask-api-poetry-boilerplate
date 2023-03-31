"""
Home App Tests
"""


def test_initial_response(create_test_client, create_test_app) -> None:
    """
    Test app's response
    """
    response = create_test_client.get("/")
    body = response.get_data()
    assert "Hello World!" in str(body)
    assert create_test_app.config.DB_HOST == "testing-db"
