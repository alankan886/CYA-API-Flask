from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, fresh_jwt_required, get_jwt_identity

from ..models.board import BoardModel
from ..models.user import UserModel
from ..schemas.board import BoardSchema


NAME_ALREADY_EXISTS = "A board with name '{}' already exists."
BOARD_NOT_FOUND = "Board not found."
BOARD_DELETED = "Board deleted."
ERROR_INSERTING = "An error occurred while inserting the board."
NO_REQUEST_BODY = "No update due to empty request body."
INCORRECT_USERNAME = "Incorrect username."

board_schema = BoardSchema(load_only=("cards.card_sm_info",))
board_list_schema = BoardSchema(many=True, load_only=("cards",))


class Board(Resource):
    @classmethod
    @jwt_required
    def get(cls, board_name: str, username: str):
        user = UserModel.find_by_username(username)
        if user.id != get_jwt_identity():
            return {'message': INCORRECT_USERNAME}, 400
        
        board = BoardModel.find_by_name(board_name, user.id)
        
        if board:
            return board_schema.dump(board), 200
        
        return {"message": BOARD_NOT_FOUND}, 404

    @classmethod
    @jwt_required
    def post(cls, board_name: str, username: str):
        user = UserModel.find_by_username(username)
        if user.id != get_jwt_identity():
            return {'message': INCORRECT_USERNAME}, 400

        board = BoardModel.find_by_name(board_name, user.id)
        
        if board:
            return {"message" : NAME_ALREADY_EXISTS.format(board_name)}, 400
        
        board = BoardModel(name=board_name, user_id=user.id)

        try:
            board.save_to_db()
        except:
            return {"message" : ERROR_INSERTING}, 500
        
        return board_schema.dump(board), 201

    @classmethod
    @fresh_jwt_required
    def put(cls, board_name: str, username: str):
        user = UserModel.find_by_username(username)
        if user.id != get_jwt_identity():
            return {'message': INCORRECT_USERNAME}, 400

        board = BoardModel.find_by_name(board_name, user.id)

        board_json = request.get_json()

        if board:
            if not board_json:
                return {"message": NO_REQUEST_BODY}, 400

            name_already_exists = BoardModel.find_by_name(board_json["name"], user.id) != None

            if name_already_exists:
                return {"message": NAME_ALREADY_EXISTS.format(board_json["name"])}, 400
            
            if "name" in board_json:
                board.name = board_json["name"]
        else:
            board_json["name"] = board_name
            board_json["user_id"] = user.id

        try:
            board.save_to_db()
        except:
            return {"message" : ERROR_INSERTING}, 500

        return board_schema.dump(board), 201
    
    @classmethod
    @fresh_jwt_required
    def delete(cls, board_name: str, username: str):
        user = UserModel.find_by_username(username)
        if user.id != get_jwt_identity():
            return {'message': INCORRECT_USERNAME}, 400

        board = BoardModel.find_by_name(board_name, user.id)
        
        if board:
            board.delete_from_db()
            return {"message" : BOARD_DELETED}, 200

        return {"message": BOARD_NOT_FOUND}, 404


class BoardList(Resource):
    @classmethod
    @jwt_required
    def get(cls, username: str):
        user = UserModel.find_by_username(username)
        if user.id != get_jwt_identity():
            return {'message': INCORRECT_USERNAME}, 400

        return {'boards' : board_list_schema.dump(BoardModel.find_all(user.id))}, 200