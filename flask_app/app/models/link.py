from app.extensions import db
from . import visitor
from datetime import datetime

class Link(db.Model):
    link_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link_name = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    url_reduced = db.Column(db.String(100), nullable=False)
    isvisible = db.Column(db.Boolean)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.influencer_id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<Link "{self.link_name}">'