from typing import List
from datetime import date

from sqlalchemy import desc 

from ..extensions.db import db


class CardModel(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(80), nullable=False)
    tag = db.Column(db.String(80))
    quality = db.Column(db.Integer, nullable=False)
    last_review = db.Column(db.Date, default=date.today)
    next_review = db.Column(db.Date)

    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'), nullable=False)

    card_sm_info = db.relationship('CardSMInfoModel', backref='card', cascade="all, delete")

    @classmethod
    def find_by_name(cls, name: str, board_id: int) -> 'CardModel':
        return cls.query.filter_by(name=name, board_id=board_id).first()
    
    @classmethod
    def find_all(cls, kwargs) -> List['CardModel']:
        board_ids = kwargs["board_ids"]

        if len(kwargs) > 1:
            next_review = kwargs["next_review"]
            return cls.query.filter(cls.board_id.in_(board_ids), cls.next_review==cls.next_review <= next_review).all()
        else:
            return cls.query.filter(cls.board_id.in_(board_ids)).all()

    @classmethod
    def find_all_by_board_id(cls, board_id: int) -> List['CardModel']:
        return cls.query.filter_by(board_id=board_id).all()
    
    @classmethod
    def find_all_by_date_and_board(cls, next_review: date, board_id: int) -> List['CardModel']:
        return cls.query.filter(cls.next_review==cls.next_review <= next_review, cls.board_id==board_id).all()
    
    @classmethod
    def find_next_card_id(cls):
        return cls.query.order_by(cls.id.desc()).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

