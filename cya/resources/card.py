from flask_restful import Resource, reqparse
from flask_restx import inputs
from flask_jwt import jwt_required
from models.card import CardModel

class Card(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('tag',
                        type=str,
                        help="A tag must be a string."
                        )

    #parser.add_argument('last_checked',
    #                    type=inputs.date,
    #                    help = "Last Checked must be a valid date."
    #                    )

    #parser.add_argument('next_check',
    #                    type=inputs.date,
    #                    help = "Next Check should be a future date."
    #                    )

    parser.add_argument('board_id',
                        type=int,
                        required=True,
                        help="Every card needs a board_id, aka the board which the card belongs to."
                        )

    def get(self, name):
        card = CardModel.find_by_name(name)
        if card:
            return card.json()
        
        return {'message' : 'Card not found.'}, 404

    def post(self, name):
        if CardModel.find_by_name(name):
            return {'message' : "A card with name '{}' already exists.".format(name)}, 400
        
        data = Card.parser.parse_args()

        card = CardModel(name, **data)

        try:
            card.save_to_db()
        except:
            return {'message' : 'An error occurred inserting the item.'}, 500
        
        return card.json(), 201

    def put(self, name):
        data = Card.parser.parse_args()

        card = CardModel.find_by_name(name)

        if card:
            card.tag = data['tag']
            #card.last_checked = data['last_checked']
            #card.next_check = data['next_check']
            card.board_id = data['board_id']
        else:
            card = CardModel(name, **data)
        
        card.save_to_db()

        return card.json()

    def delete(self, name):
        card = CardModel.find_by_name(name)
        if card:
            card.delete_from_db()
            return {'message' : 'Card deleted.'}
        
        return {'message' : 'Card not found.'}, 404

class CardList(Resource):
    def get(self):
        return {'cards' : list(map(lambda x: x.json(), CardModel.query.all()))}