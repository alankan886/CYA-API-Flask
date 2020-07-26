from datetime import date

from supermemo2 import SMTwo

from ..extensions.db import db


class CardSMInfoModel(db.Model):
    __tablename__ = 'card_sm_info'

    id = db.Column(db.Integer, primary_key=True)
    quality = db.Column(db.Integer, nullable=False)
    new_interval = db.Column(db.Integer, nullable=False)
    new_repetitions = db.Column(db.Integer, nullable=False)
    new_easiness = db.Column(db.Float, nullable=False)
    next_review = db.Column(db.Date, nullable=False)
    last_review = db.Column(db.Date, default=date.today)

    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)

    @classmethod
    def find_by_id(cls, id: int) -> 'CardSMInfoModel':
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_latest_review(cls, card_id: int) -> 'CardSMInfoModel':
        return cls.query.filter_by(card_id=card_id).order_by(cls.last_review.desc()).first()

    @classmethod
    def calc_sm_info(cls, quality, first_visit, new_interval=None, new_repetitions=None, new_easiness=None, last_review=date.today()):
        if first_visit:
            sm_two = SMTwo(quality=quality, first_visit=True, last_review=last_review)
        else:
            # TODO: This might be wrong, because I would need to search up the latest record, then pass those values.
            sm_two = SMTwo(
                quality=quality,
                interval=new_interval,
                repetitions=new_repetitions,
                easiness=new_easiness,
                last_review=last_review)

        return sm_two
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()