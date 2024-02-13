from datetime import datetime
from app.extensions import db
from sqlalchemy.dialects.postgresql import JSONB

class Visitor(db.Model):
    __tablename__ = 'visitor'
    visitor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.influencer_id'), nullable=False)
    referer = db.Column(db.Text)
    location = db.Column(db.String(100))
    link_id = db.Column(db.Integer, db.ForeignKey('link.link_id'), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.utcnow())
    headers = db.Column(JSONB, default={})
    
    def __repr__(self):
        return f'<Visitor "{self.visitor_id}">'
    
