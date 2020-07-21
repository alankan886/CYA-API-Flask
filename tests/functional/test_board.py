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
def test_valid_get_by_board_name(id, username, password, boards, test_client, init_database, auth_tokens):
    for board in boards:
        response = test_client.get(
            '/{username}/{board_name}'.format(username=username, board_name=board),
            headers={"authorization": "Bearer {}".format(auth_tokens.access_tokens[id-1])}
        )

        response_data = json.loads(response.data)

        assert response.status_code == 200

@pytest.mark.parametrize(attr_names, board_post_board_by_id_test_info)
def test_valid_post_by_board_name(id, username, password, boards, test_client, init_database, auth_tokens):
    for board in boards:
        response = test_client.post(
            '/{username}/{board_name}'.format(username=username, board_name=board),
            headers={"authorization": "Bearer {}".format(auth_tokens.access_tokens[id-1])}
        )

        response_data = json.loads(response.data)

        assert response.status_code == 201
        assert response_data['name'] == board
        assert response_data['user_id'] == id
        assert response_data['cards'] == []
