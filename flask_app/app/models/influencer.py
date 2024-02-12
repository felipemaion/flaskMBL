from app.extensions import db
from datetime import datetime
from . import link
# class Influencer(db.Model):
#     __tablename__ = 'influencer'
#     influencer_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     url = db.Column(db.String(255))
#     created_at = db.Column(db.DateTime)

#     links = db.relationship('Link', backref='influencer', lazy=True)
#     visitors = db.relationship('Visitor', backref='influencer', lazy=True)
    
#     def __repr__(self):
#         return f'<Influencer "{self.title}">'
    
    
class Influencer(db.Model):
    __tablename__ = 'influencer'
    influencer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)

    # links = db.relationship('Link', backref='influencer_obj', lazy=True, cascade="all, delete-orphan") # Changed backref name
    # visitors = db.relationship('Visitor', backref='influencer', lazy=True)

    def __repr__(self):
        return f'<Influencer "{self.name}">'
