from . import main
from ...extensions.db import db

@main.before_app_first_request
def create_tables():
    db.create_all()