from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required

from models.card import CardModel
from schemas.card import CardSchema

NAME_ALREADY_EXISTS = "An card with name '{}' already exists."
CARD_NOT_FOUND = "Card not found."
CARD_DELETED = "Card deleted."
ERROR_INSERTING = "An error occurred while inserting the item."

card_schema = CardSchema()
card_list_schema = CardSchema(many=True)

class Card(Resource):
    @classmethod
    def get(cls, name: str):
        card = CardModel.find_by_name(name)
        if card:
            return card_schema.dump(card), 200
        
        return {"message" : CARD_NOT_FOUND}, 404

    @classmethod
    def post(cls, name: str):
        if CardModel.find_by_name(name):
            return {"message" : NAME_ALREADY_EXISTS.format(name)}, 400
        
        card_json = request.get_json()
        card_json["name"] = name

        card = card_schema.load(card_json)

        try:
            card.save_to_db()
        except:
            return {"message" : ERROR_INSERTING}, 500
        
        return card_schema.dump(card), 201

    @classmethod
    def put(cls, name: str):
        card_json = request.get_json()
        card = CardModel.find_by_name(name)

        if card:
            card.tag = card_json['tag']
            card.last_checked = card_json['last_checked']
        else:
            card_json["name"] = name
            card = card_schema.load(card_json)
        
        card.save_to_db()

        return card_schema.dump(card), 200

    @classmethod
    def delete(cls, name: str):
        card = CardModel.find_by_name(name)
        if card:
            card.delete_from_db()
            return {"message" : CARD_DELETED}, 200
        
        return {"message" : CARD_NOT_FOUND}, 404


class CardList(Resource):
    @classmethod
    def get(cls):
        return {'cards' : card_list_schema.dump(CardModel.find_all())}, 200