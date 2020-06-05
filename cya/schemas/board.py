from ma import ma
from models.board import BoardModel
from models.card import CardModel
from schemas.card import CardSchema

class BoardSchema(ma.ModelSchema):
    items = ma.Nested(CardSchema, many=True)

    class Meta:
        model = BoardModel
        dump_only = ("id",)
        include_fk = True