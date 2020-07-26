import json
from random import choice

import pytest

from ..conftest import (
    test_client,
    init_database,
    auth_tokens
)

from ..test_cases import (
    attr_names,
    users_info,
    invalid_users_info,
    board_post_board_by_id_test_info
)

@pytest.mark.parametrize(attr_names, users_info)
def test_valid_get_boards(id, username, password, boards, test_client, init_database, auth_tokens):
    response = test_client.get(
        '/boards',
        headers={"authorization": "Bearer {}".format(auth_tokens.access_tokens[id-1])}
    )

    response_data = json.loads(response.data)
    
    assert response.status_code == 200

    i = 0
    for board in response_data['boards']:
        assert board['name'] == boards[i][1]
        assert board['user_id'] == id
        assert board['id'] == boards[i][0]
        i += 1

@pytest.mark.parametrize(attr_names, users_info)
def test_valid_get_by_board_name(id, username, password, boards, test_client, init_database, auth_tokens):

    for board in boards:
        board_id = board[0]
        board_name = board[1]
        response = test_client.get(
            '/{board_name}'.format(board_name=board_name),
            headers={"authorization": "Bearer {}".format(auth_tokens.access_tokens[id-1])}
        )

        response_data = json.loads(response.data)
        
        assert response.status_code == 200
        assert response_data['name'] == board_name
        assert response_data['user_id'] == id
        assert response_data['id'] == board_id
        assert 'cards' in response_data
        

@pytest.mark.parametrize(attr_names, board_post_board_by_id_test_info)
def test_valid_post_by_board_name(id, username, password, boards, test_client, init_database, auth_tokens):
    for board in boards:
        board_id = board[0]
        board_name = board[1]
        response = test_client.post(
            '/{board_name}'.format(board_name=board_name),
            headers={"authorization": "Bearer {}".format(auth_tokens.access_tokens[id-1])}
        )

        response_data = json.loads(response.data)

        assert response.status_code == 201
        assert response_data['name'] == board_name
        assert response_data['user_id'] == id
        assert response_data['id'] == board_id
        assert response_data['cards'] == []
