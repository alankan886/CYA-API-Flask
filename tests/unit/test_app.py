from flask import current_app

from ..conftest import app

def test_app_exists(app):
    with app.app_context():
        assert current_app is not None

def test_app_is_testing(app):
    with app.app_context():
        assert current_app.config["TESTING"] == True