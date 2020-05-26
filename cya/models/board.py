from db import db
from datetime import datetime

class BoardModel(db.Model):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime)

    cards = db.relationship('CardModel')

    def __init__(self, name, created_date, last_modified):
        self.name = name
        self.created_date = created_date
        self.last_modified = last_modified

    def json(self):
        return {'name' : self.name, 'cards': [card.json() for card in cards], 'created_date' : self.created_date, 'last modified' : self.last_modified}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()