from ... import api
from ...resources.card import Card, CardList, CardsDueToday, CardsDueTodayOnBoard
from ...resources.board import Board, BoardList
from ...resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from ...resources.card_sm_info import CardSMInfo, CardSMInfoId, CardSMInfoList

api.add_resource(Card, "/<string:username>/<string:board_name>/<string:card_name>")
api.add_resource(CardList, "/<string:username>/<string:board_name>/cards")
api.add_resource(CardsDueToday, "/<string:username>/cards/today")
api.add_resource(CardsDueTodayOnBoard, "/<string:username>/<string:board_name>/cards/today")

api.add_resource(CardSMInfo, "/<string:username>/<string:board_name>/<string:card_name>/sm2-info")
api.add_resource(CardSMInfoId, "/<string:username>/<string:board_name>/<string:card_name>/sm2-info/<int:id>")
api.add_resource(CardSMInfoList, "/<string:username>/<string:board_name>/<string:card_name>/all-sm2-info")

api.add_resource(Board, "/<string:username>/<string:board_name>")
api.add_resource(BoardList, "/<string:username>/boards")

api.add_resource(UserRegister, "/register")
api.add_resource(User, "/users/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")

