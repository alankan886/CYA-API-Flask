from ..extensions.ma import ma
from ..models.card import CardModel
from ..models.board import BoardModel
from ..models.card_sm_info import CardSMInfoModel
from ..schemas.card_sm_info import CardSMInfoSchema

class CardSchema(ma.SQLAlchemyAutoSchema):
    card_sm_info = ma.Nested(CardSMInfoSchema, many=True)

    class Meta:
        model = CardModel
        load_only = ('board', 'quality')
        include_fk = True
        load_instance = True