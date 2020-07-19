import pytest

from flask_jwt_extended import create_access_token

from app import create_app
from app.extensions.db import db
from app.models.user import UserModel

class AuthTokens:
    def __init__(self):
        self.access_tokens = []
        self.refresh_tokens = []


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
def init_database(request, app):
    db.create_all()
    
    yield db

    # If the session isn't closed, the test_client for some reason won't be able to shut down.
    db.session.close()
    db.drop_all()

@pytest.fixture(scope="session")
def auth_tokens():
    return AuthTokens()
    