from typing import List
import datetime

from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from ..models.card_sm_info import CardSMInfoModel
from ..models.card import CardModel
from ..models.board import BoardModel
from ..models.user import UserModel
from ..schemas.card_sm_info import CardSMInfoSchema


USER_NOT_FOUND = "User not found."
BOARD_NOT_FOUND = "Board not found."
CARD_NOT_FOUND = "Card not found."
ERROR_INSERTING = "An error occurred while inserting the item."
CANNOT_MODIFY = "{} cannot be directly modified since they are not a user input, they are calculated by the algorithm."
CARD_SM_INFO_DELETED = "Card's SuperMemo2 information of 'id={}' deleted."
CARD_SM_INFO_NOT_FOUND = "Card's SuperMemo2 information of 'id={}' not found."


card_sm_info_schema = CardSMInfoSchema()
card_sm_info_schema_list = CardSMInfoSchema(many=True)


class CardSMInfo(Resource):
    @classmethod
    @jwt_required
    @swag_from("swagger_ui/card_sm_info/card_sm_info_post_by_card.yml")
    def post(cls, card_name: str, board_name: str) -> List[dict]:
        user = UserModel.find_by_id(get_jwt_identity())
        
        board = BoardModel.find_by_name(board_name, user.id)
            
        if not board:
            return {"message": BOARD_NOT_FOUND}, 404
        
        card = CardModel.find_by_name(card_name, board.id)
        
        if not card:
            return {"message": CARD_NOT_FOUND}, 404

        quality = request.get_json()["quality"]

        latest_card_sm_info = CardSMInfoModel.find_latest_review(card.id)
        
        if latest_card_sm_info:
            new_card_sm_info = CardSMInfoModel.calc_sm_info(
                quality,
                False,
                latest_card_sm_info.new_interval,
                latest_card_sm_info.new_repetitions,
                latest_card_sm_info.new_easiness,
                latest_card_sm_info.next_review
            )
        else:
            new_card_sm_info = CardSMInfoModel.calc_sm_info(
                quality,
                True
            )
       
        new_card_sm_json = new_card_sm_info.json()
        new_card_sm_json["quality"] = quality
        new_card_sm_json["last_review"] = str(new_card_sm_info.last_review)
        new_card_sm_json["card_id"] = card.id

        # Marshallow is able to convert valid date string to date object when you load it.
        # So its' import to serialize the data here.
        new_card_sm_info = card_sm_info_schema.load(new_card_sm_json)

        try:
            new_card_sm_info.save_to_db()
        except:
            return {"message" : ERROR_INSERTING}, 500

        return card_sm_info_schema.dump(new_card_sm_info), 201

class CardSMInfoId(Resource):
    @classmethod
    @jwt_required
    @swag_from("swagger_ui/card_sm_info/card_sm_info_put_by_sm_id.yml")
    def put(cls, id:int, card_name: str, board_name: str) -> List[dict]:
        new_card_sm_info = None

        user = UserModel.find_by_id(get_jwt_identity())
        
        board = BoardModel.find_by_name(board_name, user.id)
            
        if not board:
            return {"message": BOARD_NOT_FOUND}, 404
        
        
        card = CardModel.find_by_name(card_name, board.id)
        if not card:
            return {"message": CARD_NOT_FOUND}, 404


        card_sm_json = request.get_json()
        # TODO: Wrong, this only chagnes the first record, we need specific ids
        card_sm_info = CardSMInfoModel.find_by_id(id)

        no_update_list = ["new_easiness", "new_interval", "next_review", "new_repetitions"]
        quality_changed = False
        last_review_changed = False

        if card_sm_info:
            for attribute in card_sm_json:
                if attribute in no_update_list:
                    return {"message": CANNOT_MODIFY.format(attribute)}
                
                if attribute == "quality":
                    quality_changed = True
                elif attribute == "last_review":
                    last_review_changed = True
                
                setattr(card_sm_info, attribute, card_sm_json[attribute])

            if quality_changed:
                # We want a copy of the __dict__ of card_sm_info, because sqlalchemy uses it to do things, like session save to db, we want to leave the original one clean.
                arguments = vars(card_sm_info).copy()
                unwanted_attributes = ["_sa_instance_state", "id", "card_id", "next_review"]

                for attribute in unwanted_attributes:
                    del arguments[attribute]
                
                arguments["first_visit"] = False
                
                # TODO: This part might be wrong because we have to take the return object of calc_sm_info
                card_sm_info = card_sm_info.calc_sm_info(**arguments)

            if last_review_changed:
                card_sm_info.next_review =  datetime.datetime.strptime(card_sm_json["last_review"], "%Y-%m-%d") + datetime.timedelta(days=card_sm_info.new_interval)
            
            # TODO: There's a big here
            card_sm_json = card_sm_info.json()
            card_sm_json["quality"] = card_sm_info.quality
            card_sm_json["last_review"] = str(card_sm_info.last_review)
            card_sm_json["card_id"] = card.id
            card_sm_info = card_sm_info_schema.load(card_sm_json)
        else:
            latest_card_sm_info = CardSMInfoModel.find_latest_review(card.id)
            quality = card_sm_json["quality"]
            if latest_card_sm_info:
                new_card_sm_info = CardSMInfoModel.calc_sm_info(
                    quality,
                    False,
                    latest_card_sm_info.new_interval,
                    latest_card_sm_info.new_repetitions,
                    latest_card_sm_info.new_easiness,
                    latest_card_sm_info.next_review
                )
            else:
                new_card_sm_info = CardSMInfoModel.calc_sm_info(
                    quality,
                    True
                )

            # If you can the class attribute name like remvoing 'new_', this json part will cause error.
            new_card_sm_json = new_card_sm_info.json()
            new_card_sm_json["quality"] = quality
            new_card_sm_json["last_review"] = str(new_card_sm_info.last_review)
            new_card_sm_json["card_id"] = card.id

            # Marshallow is able to convert valid date string to date object when you load it.
            # So its' import to serialize the data here.
            card_sm_info = card_sm_info_schema.load(new_card_sm_json)

        
        try:
            card_sm_info.save_to_db()
        except:
            return {"message" : ERROR_INSERTING}, 500
        
        return card_sm_info_schema.dump(card_sm_info), 200 if not new_card_sm_info else 201

    @classmethod
    @jwt_required
    @swag_from("swagger_ui/card_sm_info/card_sm_info_delete_by_sm_id.yml")
    def delete(cls, id: int, card_name: str, board_name:str) -> str:
        user = UserModel.find_by_id(get_jwt_identity())
        
        board = BoardModel.find_by_name(board_name, user.id)
            
        if not board:
            return {"message": BOARD_NOT_FOUND}, 404
        
        card = CardModel.find_by_name(card_name, board.id)
        if not card:
            return {"message": CARD_NOT_FOUND}, 404

        card_sm_info = CardSMInfoModel.find_by_id(id)
        
        if card_sm_info:
            card_sm_info.delete_from_db()
            return {"message" : CARD_SM_INFO_DELETED.format(id)}, 200
        
        return {"message" : CARD_SM_INFO_NOT_FOUND.format(id)}, 404

    
class CardSMInfoList(Resource):
    @classmethod
    @jwt_required
    @swag_from("swagger_ui/card_sm_info/card_sm_info_get_all_by_card.yml")
    def get(cls, card_name: str, board_name: str) -> List[dict]:
        user = UserModel.find_by_id(get_jwt_identity())
        
        board = BoardModel.find_by_name(board_name, user.id)
            
        if not board:
            return {"message": BOARD_NOT_FOUND}, 404
        
        card = CardModel.find_by_name(card_name, board.id)
            
        if not card:
            return {"message": CARD_NOT_FOUND}, 404

        return {"card_sm_info": card_sm_info_schema_list.dump(card.card_sm_info)}, 200