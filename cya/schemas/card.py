from ma import ma
from models.card import CardModel
from models.board import BoardModel

class CardSchema(ma.ModelSchema):
    class Meta:
        model = CardModel
        load_only = ('board',)
        dump_only = ('id',)
        include_fk = True