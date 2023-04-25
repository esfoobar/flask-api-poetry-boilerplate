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


def send_post_request(client, data):
    """send post request"""
    return client.post("/v1.0/users", data=json.dumps(data), headers=headers())


def test_user_create(create_test_client):
    """
    Test user creation
    """

    # create user
    response = send_post_request(create_test_client, user_dict())
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data["username"] == user_dict()["username"]

    # create user with same username
    response = send_post_request(create_test_client, user_dict())
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data["message"] == "Username already exists"

    # create user with same email
    test_user = user_dict()
    test_user["username"] = "jsmith2"
    response = send_post_request(create_test_client, test_user)
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data["message"] == "Email already exists"

    # missing username
    test_user = user_dict()
    del test_user["username"]
    response = send_post_request(create_test_client, test_user)
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data["errors"]["username"] == "'username' is a required property"
