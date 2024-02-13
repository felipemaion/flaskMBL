from app.extensions import db
from datetime import datetime
from . import link
    
class Influencer(db.Model):
    influencer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<Influencer "{self.name}">'
