from flask import Flask, Blueprint
from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager

from .jwt_error_handle import (
    expired_token_callback,
    invalid_token_callback,
    missing_token_callback,
    token_not_fresh_callback,
    revoked_token_callback,
)

from .db import db
from .ma import ma
from .blacklist import BLACKLIST
from config import config

# A Blueprint instance is needed here to pass to the flask-restful Api class
api_blueprint_setup = Blueprint('setup', __name__)
api = Api(api_blueprint_setup)

def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    ma.init_app(app)
    db.init_app(app)
    jwt = JWTManager(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .cya_api import api as api_blueprint
    app.register_blueprint(api_blueprint)
    app.register_blueprint(api_blueprint_setup)

    # might need to add another blueprint instance just for Api()

    @app.before_first_request
    def create_tables():
        db.create_all()
    
    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        return decrypted_token["jti"] in BLACKLIST

    # Decorating the functions
    #expired_token_callback = jwt.expired_token_loader(expired_token_callback)
    #invalid_token_callback = jwt.invalid_token_loader(invalid_token_callback)
    #missing_token_callback = jwt.unauthorized_loader(missing_token_callback)
    #token_not_fresh_callback = jwt.needs_fresh_token_loader(token_not_fresh_callback)
    #revoked_token_callback = jwt.revoked_token_loader(revoked_token_callback)

    return app