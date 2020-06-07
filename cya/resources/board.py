from flask_restful import Resource

from models.board import BoardModel
from schemas.board import BoardSchema

NAME_ALREADY_EXISTS = "A board with name '{}' already exists."
BOARD_NOT_FOUND = "Board not found."
BOARD_DELETED = "Board deleted."
ERROR_INSERTING = "An error occurred while inserting the board."

board_schema = BoardSchema()
board_list_schema = BoardSchema(many=True)


class Board(Resource):
    @classmethod
    def get(cls, name: str):
        board = BoardModel.find_by_name(name)
        if board:
            return board_schema.dump(board), 200
        
        return {"message" : BOARD_NOT_FOUND}, 404

    @classmethod
    def post(cls, name: str):
        if BoardModel.find_by_name(name):
            return {"message" : NAME_ALREADY_EXISTS.format(name)}, 400

        board = BoardModel(name=name)
        try:
            board.save_to_db()
        except:
            return {"message" : ERROR_INSERTING}, 500
        
        return board_schema.dump(board), 201

    @classmethod
    def delete(cls, name: str):
        board = BoardModel.find_by_name(name)
        if board:
            board.delete_from_db()
            return {"message" : BOARD_DELETED}, 200

        return board_schema.dump(board), 201


class BoardList(Resource):
    @classmethod
    def get(cls):
        return {'boards' : board_list_schema.dump(BoardModel.find_all())}, 200