from ... import api
from ...resources.card import Card, CardsByBoard, Cards
from ...resources.board import Board, Boards
from ...resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from ...resources.card_sm_info import CardSMInfo, CardSMInfoId, CardSMInfoList

api.add_resource(Card, "/<string:board_name>/<string:card_name>")
api.add_resource(CardsByBoard, "/<string:board_name>/cards")
api.add_resource(Cards, "/cards")

api.add_resource(CardSMInfo, "/<string:board_name>/<string:card_name>/sm2-info")
api.add_resource(CardSMInfoId, "/<string:board_name>/<string:card_name>/sm2-info/<int:id>")
api.add_resource(CardSMInfoList, "/<string:board_name>/<string:card_name>/all-sm2-info")

api.add_resource(Board, "/<string:board_name>")
api.add_resource(Boards, "/boards")

api.add_resource(UserRegister, "/register")
api.add_resource(User, "/users/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")

