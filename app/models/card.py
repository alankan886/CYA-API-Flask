from typing import List
from datetime import date

from sqlalchemy import desc 

from ..extensions.db import db


class CardModel(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(80))
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
    def find_all_by_board_id(cls, board_id: int) -> List['CardModel']:
        return cls.query.filter_by(board_id=board_id).all()
    
    @classmethod
    def find_all_by_date(cls, next_check: date) -> List['CardModel']:
        return cls.query.filter_by(next_check=next_check).all()
    
    @classmethod
    def find_all_by_date_and_board(cls, next_check: date, board_id: int) -> List['CardModel']:
        return cls.query.filter_by(next_check=next_check, board_id=board_id).all()
    
    @classmethod
    def find_next_card_id(cls, board_id: int):
        return cls.query.filter_by(board_id=board_id).order_by(cls.id.desc()).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

