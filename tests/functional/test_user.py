import json

import pytest

from ..conftest import (
    test_client,
    init_database,
    auth_tokens
)

from ..test_cases import attr_names, users_info, invalid_users_info, user_post_register_test_info

@pytest.mark.parametrize(attr_names, user_post_register_test_info)
def test_valid_user_post_register(id, username, password, boards, test_client, init_database):
    response = test_client.post('/register',
        content_type='application/json',
        json={"username": username, "password": password}
    )
    
    response_data = json.loads(response.data)
    
    assert response.status_code == 201
    assert len(response_data) == 1
    assert response_data["message"] == "User created successfully."

@pytest.mark.parametrize(attr_names, users_info)
def test_invalid_user_post_register(id, username, password, boards, test_client, init_database):
    response = test_client.post('/register',
        content_type='application/json',
        json={'username': username, 'password': password}
    )

    response_data = json.loads(response.data)
    
    assert response.status_code == 400
    assert response_data['message'] == "A user with the same username already exists."

@pytest.mark.parametrize(attr_names, users_info)
def test_valid_user_post_login(id, username, password, boards, test_client, init_database, auth_tokens):
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

@pytest.mark.parametrize(attr_names, invalid_users_info)
def test_invalid_user_post_login(id, username, password, boards, test_client, init_database, auth_tokens):
    response = test_client.post('/login',
        content_type='application/json',
        json={"username": username, "password": password}
    )

    response_data = json.loads(response.data)

    assert response.status_code == 401
    assert response_data['message'] == 'Invalid credentials!'

@pytest.mark.parametrize(attr_names, users_info)
def test_valid_user_post_logout(id, username, password, boards, test_client, init_database, auth_tokens):
    response = test_client.post('/logout',
        headers={"authorization": "Bearer {}".format(auth_tokens.access_tokens[id-1])}
    )

    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert response_data["message"] == "User {} successfully logged out.".format(username)

@pytest.mark.parametrize(attr_names, users_info)
def test_valid_user_post_refresh(id, username, password, boards, test_client, init_database, auth_tokens):
    response = test_client.post('/refresh',
        headers={"authorization": "Bearer {}".format(auth_tokens.refresh_tokens[id-1])}
    )

    response_data = json.loads(response.data)

    assert response.status_code == 200

@pytest.mark.parametrize(attr_names, users_info)
def test_valid_user_get_by_id(id, username, password, boards, test_client, init_database):
    response = test_client.get('/users/{}'.format(id))

    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["id"] == id
    assert response_data["username"] == username

@pytest.mark.parametrize(attr_names, invalid_users_info)
def test_invalid_user_get_by_id(id, username, password, boards, test_client, init_database):
    response = test_client.get('/users/{}'.format(id))

    response_data = json.loads(response.data)

    assert response.status_code == 404
    assert response_data['message'] == 'User not found.'

@pytest.mark.parametrize(attr_names, users_info)
def test_valid_user_delete_by_id(id, username, password, boards, test_client, init_database):
    response = test_client.delete('/users/{}'.format(id))

    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["message"] == "User deleted."

@pytest.mark.parametrize(attr_names, invalid_users_info)
def test_invalid_user_delete_by_id(id, username, password, boards, test_client, init_database):
    response = test_client.delete('/users/{}'.format(id))

    response_data = json.loads(response.data)

    assert response.status_code == 404
    assert response_data["message"] == "User not found."