from typing import List
from datetime import date

from db import db

class CardModel(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    tag = db.Column(db.String(80))
    last_checked = db.Column(db.Date, default=date.today)
    next_check = db.Column(db.Date, nullable=False)

    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'), nullable=False)

    @classmethod
    def find_by_name(cls, name: str, board_id: int) -> 'CardModel':
        return cls.query.filter_by(name=name, board_id=board_id).first()
    
    @classmethod
    def find_all(cls, board_id: int) -> List['CardModel']:
        return cls.query.filter_by(board_id=board_id).all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

