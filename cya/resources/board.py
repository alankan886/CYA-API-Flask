from flask_restful import Resource
from models.board import BoardModel


class Board(Resource):
    def get(self, name):
        board = BoardModel.find_by_name(name)
        if board:
            return board.json()
        
        return {'message' : 'Board not found.'}, 404

    def post(self, name):
        if BoardModel.find_by_name(name):
            return {'message' : "A board with name '{}' already exists.".format(name)}, 400

        board = BoardModel(name)
        try:
            board.save_to_db()
        except:
            return {'message' : 'An error occurred creating the board.'}, 500
        
        return board.json(), 201

    def put(self, name):
        pass

    def delete(self, name):
        board = BoardModel.find_by_name(name)
        if board:
            board.delete_from_db()
        
        return {'message' : 'Board deleted.'}

class BoardList(Resource):
    def get(self):
        return {'boards' : list(map(lambda x: x.json(), BoardModel.query.all()))}