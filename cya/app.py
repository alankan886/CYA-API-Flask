from flask import Flask
from flask_restful import Api, Resource
from resources.card import Card
from resources.board import Board
from resources.user import UserRegister
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


api.add_resource(Card, '/card/<string:name>')
api.add_resource(Board, '/board')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
 