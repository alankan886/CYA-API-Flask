import json

from .conftest import test_client, init_database

def test_valid_login(test_client, init_database):
    response = test_client.post('/login', content_type='application/json',
        json={"username": "testusername1", "password": "testpassword1"}
        )
    
    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert len(response_data) > 0
    assert response_data["username"] == "testusername1"
    assert "access_token" in response_data
    assert "refresh_token" in response_data

