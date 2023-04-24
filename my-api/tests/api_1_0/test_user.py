"""
Test User API v1.0
"""

import json


def headers():
    """json headers for all requests"""
    return {"Content-Type": "application/json"}


def user_dict():
    """user dict for all requests"""
    return {
        "username": "jsmith",
        "email": "jsmith@example.com",
        "password": "test123",
    }


def test_user_create(create_test_client):
    """
    Test user creation
    """
    response = create_test_client.post(
        "/v1.0/users",
        data=json.dumps(user_dict()),
        headers=headers(),
    )
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data["username"] == user_dict()["username"]
