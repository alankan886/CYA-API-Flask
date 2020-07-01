from typing import List

from ..extensions.db import db

class BoardModel(db.Model):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    cards = db.relationship('CardModel', backref='board', cascade="all, delete")

    @classmethod
    def find_by_name(cls, name: str, user_id: int) -> 'BoardModel':
        return cls.query.filter_by(name=name, user_id=user_id).first()
    
    @classmethod
    def find_all(cls, user_id: int) -> List['BoardModel']:
        return cls.query.filter_by(user_id=user_id).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()