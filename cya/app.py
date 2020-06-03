from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT
from flask_migrate import Migrate

from auth import authenticate, identity
from resources.card import Card, CardList
from resources.board import Board, BoardList
from resources.user import UserRegister
from db import db
import env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost:3306/{}'.format(env.username, env.password, 'cyaDB')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Card, '/card/<string:name>')
api.add_resource(CardList, '/cards')
api.add_resource(Board, '/board/<string:name>')
api.add_resource(BoardList, '/boards')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
 