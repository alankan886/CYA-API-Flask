from ..extensions.ma import ma
from ..models.card_sm_info import CardSMInfoModel

class CardSMInfoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CardSMInfoModel
        dump_only = ("id",)
        include_fk = True
        load_instance = True