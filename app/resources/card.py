from datetime import date

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, fresh_jwt_required, get_jwt_identity
from flasgger import swag_from

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
BAD_QUALITY_UPDATE = "quality should be updated through card_sm_info, if the card already exists."
BAD_LAST_REVIEW_UPDATE = "last_review should be modified through the card_sm_info record, if the card already exists."
BAD_NEXT_REVIEW_UDPATE = "next_review is calculated and should not be modified through by user, if the card already exists."
INCORRECT_USERNAME = "Incorrect username."
QUALITY_MISSING = "quality is not provide, it's an required attribute."


bad_update = {"quality": ({"message": BAD_QUALITY_UPDATE}, 400), "last_review": ({"message": BAD_LAST_REVIEW_UPDATE}, 400), "next_review": ({"message": BAD_NEXT_REVIEW_UDPATE}, 400)}


card_schema = CardSchema()
card_list_schema = CardSchema(many=True, load_only=("card_sm_info",))
card_sm_info_schema = CardSMInfoSchema()


def create_new_card(card_name: str, board: 'BoardModel'):
    latest_card = CardModel.find_next_card_id()
    if latest_card:
        new_card_id = latest_card.id + 1
    else:
        new_card_id = 1

    card_json = request.get_json()
    
    if "quality" not in card_json:
        return {"message": QUALITY_MISSING}, 400
    
    card_json["name"] = card_name
    card_json["board_id"] = board.id
    card_json["id"] = new_card_id

    quality = card_json["quality"]

    if "last_review" in card_json:
        last_review = card_json["last_review"]
        card_sm_info = CardSMInfoModel.calc_sm_info(quality=quality, first_visit=True, last_review=last_review)
    else:
        card_sm_info = CardSMInfoModel.calc_sm_info(quality=quality, first_visit=True)
    
    next_review = card_sm_info.next_review
    last_review = str(card_sm_info.last_review)

    card_json["next_review"] = next_review
    card = card_schema.load(card_json)
    
    card_sm_json = card_sm_info.json()
    card_sm_json["quality"] = quality
    card_sm_json["last_review"] = last_review
    card_sm_json["card_id"] = new_card_id
    card_sm_info = card_sm_info_schema.load(card_sm_json)

    return card, card_sm_info


class Card(Resource):
    @classmethod
    @jwt_required
    @swag_from("swagger_ui/card/card_get_card_by_name.yml")
    def get(cls, card_name: str, board_name: str):
        user = UserModel.find_by_id(get_jwt_identity())
        
        board = BoardModel.find_by_name(board_name, user.id)
        if not board:
            return {"message": BOARD_NOT_FOUND }, 404

        card = CardModel.find_by_name(card_name, board.id)

        if card:
            return card_schema.dump(card), 200
        
        return {"message" : CARD_NOT_FOUND}, 404
    
    @classmethod
    @jwt_required
    @swag_from("swagger_ui/card/card_post_card_by_name.yml")
    def post(cls, card_name: str, board_name: str):
        user = UserModel.find_by_id(get_jwt_identity())
        
        board = BoardModel.find_by_name(board_name, user.id)

        if not board:
            return {"message": BOARD_NOT_FOUND }, 404

        if CardModel.find_by_name(card_name, board.id):
            return {"message": NAME_ALREADY_EXISTS.format(card_name)}, 400
        
        response = create_new_card(card_name, board)
        
        if type(response[0]) is dict:
            message = response[0]
            status_code = response[1]
            return message, status_code

        card, card_sm_info = response[0], response[1]
        print(card_sm_info)
        try:
            card.save_to_db()
            card_sm_info.save_to_db()
        except:
            return {"message" : ERROR_INSERTING}, 500
        
        return card_schema.dump(card), 201

    @classmethod
    @fresh_jwt_required
    @swag_from("swagger_ui/card/card_put_card_by_name.yml")
    def put(cls, card_name: str, board_name: str):
        card_sm_info = None

        user = UserModel.find_by_id(get_jwt_identity())

        board = BoardModel.find_by_name(board_name, user.id)
        if not board:
            return {"message": BOARD_NOT_FOUND }, 404

        card_json = request.get_json()
        card = CardModel.find_by_name(card_name, board.id)

        if card:
            for attribute in card_json:
                if attribute in bad_update:
                    message = bad_update[attribute][0]
                    status_code = bad_update[attribute][1]

                    return message, status_code
                
            if "name" in card_json:
                name_already_exists = CardModel.find_by_name(card_json["name"], board.id) != None

                if name_already_exists:
                    return {"message": NAME_ALREADY_EXISTS.format(card_json["name"])}, 400
                
                card.name = card_json["name"]

            if "tag" in card_json:
                card.tag = card_json["tag"]
        else:
            response = create_new_card(card_name, board)
        
            if type(response[0]) is dict:
                message = response[0]
                status_code = response[1]
                return message, status_code
            
            card, card_sm_info = response[0], response[1]

        try:
            card.save_to_db()
            if card_sm_info:
                card_sm_info.save_to_db()
        except:
            return {"message" : ERROR_INSERTING}, 500
        
        return card_schema.dump(card), 200 if not card_sm_info else 201

    @classmethod
    @fresh_jwt_required
    @swag_from('swagger_ui/card/card_delete_card_by_name.yml')
    def delete(cls,  card_name: str, board_name: str):
        user = UserModel.find_by_id(get_jwt_identity())

        board = BoardModel.find_by_name(board_name, user.id)
        if not board:
            return {"message": BOARD_NOT_FOUND }, 404

        card = CardModel.find_by_name(card_name, board.id)

        if card:
            card.delete_from_db()
            return {"message" : CARD_DELETED}, 200
        
        return {"message" : CARD_NOT_FOUND}, 404


class CardsByBoard(Resource):
    @classmethod
    @jwt_required
    @swag_from("swagger_ui/card/card_get_cards_by_board.yml")
    def get(cls, board_name: str):
        today = False

        user = UserModel.find_by_id(get_jwt_identity())

        board = BoardModel.find_by_name(board_name, user.id)
        if not board:
            return {"message": BOARD_NOT_FOUND }, 404
        
        if request.args:
            today = request.args["today"]

        if today:
            cards = CardModel.find_all_by_date_and_board(date.today(), board.id)
        else:
            cards = CardModel.find_all_by_board_id(board.id)

        return {"cards" : card_list_schema.dump(cards)}, 200
    
    @classmethod
    @fresh_jwt_required
    @swag_from("swagger_ui/card/card_delete_cards_by_board.yml")
    def delete(cls, board_name: str):
        user = UserModel.find_by_id(get_jwt_identity())

        board = BoardModel.find_by_name(board_name, user.id)
        if not board:
            return {"message": BOARD_NOT_FOUND }, 404
        for card in CardModel.find_all_by_board_id(board.id):
            card.delete_from_db()

        return {"message" : CARDS_DELETED}, 200

class Cards(Resource):
    @classmethod
    @jwt_required
    @swag_from("swagger_ui/card/card_get_cards.yml")
    def get(cls):
        user = UserModel.find_by_id(get_jwt_identity())
        boards = BoardModel.find_all(user.id)
        board_ids = (board.id for board in boards)
       
        query_args = {"board_ids": board_ids}

        for arg in request.args:
            if arg == "today" and request.args["today"].lower() == 'true':
                query_args["next_review"] = date.today()
        
        cards = CardModel.find_all(kwargs=query_args)

        return {"cards": card_list_schema.dump(cards)}, 200