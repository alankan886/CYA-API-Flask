from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from marshmallow import ValidationError

from resources.card import Card, CardList, CardsDueToday, CardsDueTodayOnBoard
from resources.board import Board, BoardList
from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from jwt_error_handle import (
    expired_token_callback,
    invalid_token_callback,
    missing_token_callback,
    token_not_fresh_callback,
    revoked_token_callback,
)

from db import db
from ma import ma
from blacklist import BLACKLIST


app = Flask(__name__)
app.config.from_pyfile("config.py")

api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err), 400

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST

# Decorating the functions
expired_token_callback = jwt.expired_token_loader(expired_token_callback)
invalid_token_callback = jwt.invalid_token_loader(invalid_token_callback)
missing_token_callback = jwt.unauthorized_loader(missing_token_callback)
token_not_fresh_callback = jwt.needs_fresh_token_loader(token_not_fresh_callback)
revoked_token_callback = jwt.revoked_token_loader(revoked_token_callback)


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
    ma.init_app(app)
    app.run()
 