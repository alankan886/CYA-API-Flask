import pytest

from app import create_app
from app.extensions.db import db
from app.models.user import UserModel

# @pytest.fixture(scope="function")
# def setup_config(request):
#     app = create_app("testing")
#     testing_client = app.test_client()

#     ctx = app.app_context()
#     with app.app_context():
#         db.create_all()

#         user1 = UserModel(username='testusername1', password='testpassword1')

#         db.session.add(user1)

#         db.session.commit()

#     ctx.push()

#     yield testing_client


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
def init_database(app):
    db.create_all()

    user1 = UserModel(username='testusername1', password='testpassword1')

    db.session.add(user1)
    db.session.commit()
    
    yield db

    # If the session isn't closed, the test_client for some reason won't be able to shut down.
    db.session.close()
    db.drop_all()
