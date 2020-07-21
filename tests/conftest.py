import json

import pytest
from flask_jwt_extended import create_access_token, create_refresh_token

from .test_cases import users_info
from app import create_app
from app.extensions.db import db
from app.models.user import UserModel
from app.models.board import BoardModel


class AuthTokens:
    def __init__(self):
        self.access_tokens = []
        self.refresh_tokens = []

auth = AuthTokens()


@pytest.fixture(scope="module")
def app():
    app = create_app("testing")
    return app

@pytest.fixture(scope="module")
def test_client(app):
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()
    
    yield testing_client
    
    ctx.pop()

@pytest.fixture(scope="module")
def init_database(request, app, test_client):
    db.create_all()
    
    for user_info in users_info:
        new_user = UserModel(username=user_info[1], password=user_info[2])
        
        boards = user_info[3]
        for board in boards:
            new_board = BoardModel(name=board, user_id=user_info[0])
            db.session.add(new_board)

        db.session.add(new_user)

    db.session.commit()

    yield db

    # If the session isn't closed, the test_client for some reason won't be able to shut down.
    db.session.close()
    db.drop_all()

@pytest.fixture(scope="module")
def auth_tokens(request, app):
    for user in users_info:
        with app.app_context():
            auth.access_tokens.append(create_access_token(user[0], fresh=True))
            auth.refresh_tokens.append(create_refresh_token(user[0]))
    
    return auth
    