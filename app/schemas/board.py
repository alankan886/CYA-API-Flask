from ..extensions.ma import ma
from ..models.board import BoardModel
from ..schemas.card import CardSchema

class BoardSchema(ma.SQLAlchemyAutoSchema):
    cards = ma.Nested(CardSchema, many=True)

    class Meta:
        model = BoardModel
        dump_only = ("id",)
        include_fk = True
        load_instance = True