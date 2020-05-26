from db import db

class CardModel():
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    tag = db.Column(db.String(80))
    last_checked = db.Column(db.Date)
    next_checked = db.Column(db.Date)

    def __init__(self):
        pass

    def json(self):
        pass
    
    @classmethod
    def find_by_name(cls, name):
        pass

    def save_to_db(self):
        pass

    def delete_from_db(self):
        pass

    