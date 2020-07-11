from datetime import date

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, fresh_jwt_required

from ..models.card import CardModel
from ..models.board import BoardModel
from ..models.user import UserModel
from ..models.card_sm_info import CardSMInfoModel
from ..schemas.card import CardSchema
from ..schemas.card_sm_info import CardSMInfoSchema


NAME_ALREADY_EXISTS = "An card with name '{}' already exists."
CARD_NOT_FOUND = "Card not found."
CARD_DELETED = "Card deleted."
CARDS_DELETED = "Cards deleted."
ERROR_INSERTING = "An error occurred while inserting the item."
BOARD_NOT_FOUND = "Board not found."
BAD_QUALITY_UPDATE = "Quality should be updated through card_sm_info, if the card already exists."

card_schema = CardSchema()
card_list_schema = CardSchema(many=True, load_only=("card_sm_info",))
card_sm_info_schema = CardSMInfoSchema()


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
            return {"message": BOARD_NOT_FOUND }, 404

        if CardModel.find_by_name(card_name, board.id):
            return {"message": NAME_ALREADY_EXISTS.format(card_name)}, 400
        
        latest_card = CardModel.find_next_card_id(board.id)
        if latest_card:
            new_card_id = latest_card.id + 1
        else:
            new_card_id = 1

        card_json = request.get_json()
        card_json["name"] = card_name
        card_json["board_id"] = board.id
        card_json["id"] = new_card_id

        
        last_review = None
        if "last_review" in card_json:
            last_review = card_json["last_review"]
        
        quality = card_json["quality"]
        card_sm_info = CardSMInfoModel.calc_sm_info(quality=quality, first_visit=True, last_review=last_review)
        
        next_review = card_sm_info.next_review
        last_review = str(card_sm_info.last_review)

        card_json["next_review"] = next_review
        card = card_schema.load(card_json)

        card_sm_json = card_sm_info.json()
        card_sm_json["quality"] = quality
        card_sm_json["last_review"] = last_review
        card_sm_json["card_id"] = new_card_id
        card_sm_info = card_sm_info_schema.load(card_sm_json)
        
        try:
            card.save_to_db()
            card_sm_info.save_to_db()
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
            if "quality" in card_json:
                return {"message": BAD_QUALITY_UPDATE}
                
            if "name" in card_json:
                name_already_exists = CardModel.find_by_name(card_json["name"], board.id) != None

                if name_already_exists:
                    return {"message": NAME_ALREADY_EXISTS.format(card_json["name"])}, 400
                
                card.name = card_json["name"]

            if "tag" in card_json:
                card.tag = card_json["tag"]
            
            if "last_review" in card_json:
                card.last_review = card_json["last_review"]
            
            if "next_review" in card_json:
                card.next_review = card_json["next_review"]            
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

        if board:
            cards = CardModel.find_all_by_date_and_board(date.today(), board.id)

            return {"cards": card_list_schema.dump(cards)}, 200
        
        return {"messsage": BOARD_NOT_FOUND}, 404
