from flask import Flask, Blueprint
from flask_restful import Api

from config import config


# A Blueprint instance is needed here to pass to the flask-restful Api class
# Check Flask-RESTful doc for more info
api_blueprint_setup = Blueprint('setup', __name__)
api = Api(api_blueprint_setup)


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .extensions.db import db
    db.init_app(app)

    from .extensions.ma import ma
    ma.init_app(app)

    from .extensions.migrate import migrate
    migrate.init_app(app, db)

    from .extensions.jwt import jwt
    jwt.init_app(app)

    from .blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .blueprints.jwt import jwt as jwt_blueprint
    app.register_blueprint(jwt_blueprint)

    app.register_blueprint(api_blueprint_setup)

    return app