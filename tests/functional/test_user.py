import json

import pytest

from .conftest import test_client, init_database, auth_tokens

attr_names = "id, username, password"

users = [
    (1, "testusername1", "testpassword1"),
    (2, "testusername2", "testpassword2"),
    (3, "abc", "123")
]


@pytest.mark.parametrize(attr_names, users)
def test_valid_user_post_register(id, username, password, test_client, init_database):
    response = test_client.post('/register',
        content_type='application/json',
        json={"username": username, "password": password}
    )
    
    response_data = json.loads(response.data)
    
    assert response.status_code == 201
    assert len(response_data) == 1
    assert response_data["message"] == "User created successfully."

@pytest.mark.parametrize(attr_names, users)
def test_valid_user_post_login(id, username, password, test_client, init_database, auth_tokens):
    response = test_client.post('/login',
        content_type='application/json',
        json={"username": username, "password": password}
    )
    
    response_data = json.loads(response.data)
    
    assert response.status_code == 200
    assert len(response_data) == 3
    assert response_data["username"] == username
    assert "access_token" in response_data
    assert "refresh_token" in response_data

    auth_tokens.access_tokens.append(response_data["access_token"])
    auth_tokens.refresh_tokens.append(response_data["refresh_token"])

@pytest.mark.parametrize(attr_names, users)
def test_valid_user_post_logout(id, username, password, test_client, init_database, auth_tokens):
    response = test_client.post('/logout',
        headers={"authorization": "Bearer {}".format(auth_tokens.access_tokens[id-1])}
    )

    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert response_data["message"] == "User {} successfully logged out.".format(username)

@pytest.mark.parametrize(attr_names, users)
def test_valid_user_post_refresh(id, username, password, test_client, init_database, auth_tokens):
    response = test_client.post('/refresh',
        headers={"authorization": "Bearer {}".format(auth_tokens.refresh_tokens[id-1])}
    )

    response_data = json.loads(response.data)

    assert response.status_code == 200

@pytest.mark.parametrize(attr_names, users)
def test_valid_user_get_id(id, username, password, test_client, init_database):
    response = test_client.get('/users/{}'.format(id))

    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["id"] == id
    assert response_data["username"] == username

@pytest.mark.parametrize(attr_names, users)
def test_valid_user_delete_id(id, username, password, test_client, init_database):
    response = test_client.delete('/users/{}'.format(id))

    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["message"] == "User deleted."