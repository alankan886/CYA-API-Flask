from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from marshmallow import ValidationError

from resources.card import Card, CardList, CardsDueToday, CardsDueTodayOnBoard
from resources.board import Board, BoardList
from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from db import db
from ma import ma
from blacklist import BLACKLIST
import env

application = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost:3306/{}'.format(env.username, env.password, 'cyaDB')
#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@cyadb-test.chcojzenikno.us-east-1.rds.amazonaws.com:3306/{}'.format(env.username, env.password, 'cyaDB_test')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['PROPAGATE_EXCEPTIONS'] = True
application.config['JWT_BLACKLIST_ENABLED'] = True
application.config['JWT_BLACKLIST_TOKEN_CHECKS'] = [
    "access",
    "refresh",
]
application.config['JWT_SECRET_KEY'] = env.secret_key
application.config['JWT_ACCESS_TOKEN_EXPIRES'] = 1800
api = Api(application)
db.init_app(application)
migrate = Migrate(application, db)


@application.before_first_request
def create_tables():
    db.create_all()

@application.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err), 400


jwt = JWTManager(application)


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        "description": "The token has expired.",
        "error": "token_expired"
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        "description": "Signature verification failed.",
        "error": "invalid_token"
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "description": "Request does not contain an access token.",
        "error": "authorization_required"
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        "description": "The token is not fresh.",
        "error": "fresh_token_required"
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        "description": "The token has been revoked.",
        "error": "token_revoked"
    }), 401

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST


api.add_resource(Card, "/<string:username>/<string:board_name>/<string:card_name>")
api.add_resource(CardList, "/<string:username>/<string:board_name>/cards")
api.add_resource(CardsDueToday, "/<string:username>/cards/today")
api.add_resource(CardsDueTodayOnBoard, "/<string:username>/<string:board_name>/cards/today")

api.add_resource(Board, "/<string:username>/<string:board_name>")
api.add_resource(BoardList, "/<string:username>/boards")

api.add_resource(UserRegister, "/register")
api.add_resource(User, "/users/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")


if __name__ == '__main__':
    ma.init_app(application)
    # remove debug=True in production
    # This port number should match your EB EC2 inbound port number, not sure do you need to set it.
    application.run()
 