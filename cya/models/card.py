from db import db

class CardModel(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    tag = db.Column(db.String(80))
    last_checked = db.Column(db.Date)
    next_checked = db.Column(db.Date)

    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'))
    board = db.relationship('BoardModel')

    def __init__(self, name, tag, last_checked, next_checked):
        self.name = name
        self.tag = tag
        self.last_checked = last_checked
        self.next_checked = next_checked

    def json(self):
        return {'name' : self.name, 'tag' : self.tag, 'last checked' : self.last_checked, 'next checked' : self.next_checked}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

