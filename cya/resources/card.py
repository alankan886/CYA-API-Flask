from datetime import date

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, fresh_jwt_required

from models.card import CardModel
from models.board import BoardModel
from models.user import UserModel
from schemas.card import CardSchema


NAME_ALREADY_EXISTS = "An card with name '{}' already exists."
CARD_NOT_FOUND = "Card not found."
CARD_DELETED = "Card deleted."
CARDS_DELETED = "Cards deleted."
ERROR_INSERTING = "An error occurred while inserting the item."
BOARD_NOT_FOUND = "Board not found."

card_schema = CardSchema()
card_list_schema = CardSchema(many=True)


class Card(Resource):
    @classmethod
    @jwt_required
    def get(cls, card_name: str, board_name: str, username: str):
        user = UserModel.find_by_username(username)
        board = BoardModel.find_by_name(board_name, user.id)
        card = CardModel.find_by_name(card_name, board.id)

        if card:
            return card_schema.dump(card), 200
        
        return {"message" : CARD_NOT_FOUND}, 404
    
    @classmethod
    @jwt_required
    def post(cls, card_name: str, board_name: str,username: str):
        user = UserModel.find_by_username(username)
        board = BoardModel.find_by_name(board_name, user.id)

        if not board:
            return {"message": BOARD_NOT_FOUND }

        if CardModel.find_by_name(card_name, board.id):
            return {"message": NAME_ALREADY_EXISTS.format(card_name)}, 400
        
        card_json = request.get_json()
        card_json["name"] = card_name
        card_json["board_id"] = board.id
        
        card = card_schema.load(card_json)

        try:
            card.save_to_db()
        except:
            return {"message" : ERROR_INSERTING}, 500
        
        return card_schema.dump(card), 201

    @classmethod
    @fresh_jwt_required
    def put(cls, card_name: str, board_name: str, username: str):
        user = UserModel.find_by_username(username)
        board = BoardModel.find_by_name(board_name, user.id)

        card_json = request.get_json()
        card = CardModel.find_by_name(card_name, board.id)

        if card:
            
            if "name" in card_json:
                name_already_exists = CardModel.find_by_name(card_json["name"], board.id) != None

                if name_already_exists:
                    return {"message": NAME_ALREADY_EXISTS.format(card_json["name"])}, 400
                
                card.name = card_json["name"]

            if "tag" in card_json:
                card.tag = card_json["tag"]
            
            if "last_checked" in card_json:
                card.last_checked = card_json["last_checked"]
            
            if "next_check" in card_json:
                card.next_check = card_json["next_check"]            
        else:
            card_json["name"] = card_name
            card = card_schema.load(card_json)
        
        try:
            card.save_to_db()
        except:
            return {"message" : ERROR_INSERTING}, 500
        
        return card_schema.dump(card), 200

    @classmethod
    @fresh_jwt_required
    def delete(cls,  card_name: str, board_name: str, username: str):
        user = UserModel.find_by_username(username)
        board = BoardModel.find_by_name(board_name, user.id)
        card = CardModel.find_by_name(card_name, board.id)

        if card:
            card.delete_from_db()
            return {"message" : CARD_DELETED}, 200
        
        return {"message" : CARD_NOT_FOUND}, 404


class CardList(Resource):
    @classmethod
    @jwt_required
    def get(cls, board_name: str, username: str):
        user = UserModel.find_by_username(username)
        board = BoardModel.find_by_name(board_name, user.id)

        cards = CardModel.find_all_by_board_id(board.id)

        return {"cards" : card_list_schema.dump(cards)}, 200
    
    @classmethod
    @fresh_jwt_required
    def delete(cls, board_name: str, username: str):
        user = UserModel.find_by_username(username)
        board = BoardModel.find_by_name(board_name, user.id)

        for card in CardModel.find_all_by_board_id(board.id):
            card.delete_from_db()

        return {"message" : CARDS_DELETED}

class CardsDueToday(Resource):
    @classmethod
    @jwt_required
    def get(cls, username: str):
        user = UserModel.find_by_username(username)

        cards = CardModel.find_all_by_date(date.today())

        return {"cards": card_list_schema.dump(cards)}, 200


class CardsDueTodayOnBoard(Resource):
    @classmethod
    @jwt_required
    def get(cls, board_name: str, username: str):
        user = UserModel.find_by_username(username)
        board = BoardModel.find_by_name(board_name, user.id)

        cards = CardModel.find_all_by_date_and_board(date.today(), board.id)

        return {"cards": card_list_schema.dump(cards)}, 200
