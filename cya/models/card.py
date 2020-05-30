from db import db

class CardModel(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    tag = db.Column(db.String(80))

    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'))
    board = db.relationship('BoardModel')

    def __init__(self, name, tag, board_id):
        self.name = name
        self.tag = tag
        self.board_id = board_id

    def json(self):
        return {'name' : self.name, 'tag' : self.tag, 'board_id' : self.board_id}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

