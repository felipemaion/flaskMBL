from datetime import datetime
from app.extensions import db
from sqlalchemy.dialects.postgresql import JSONB

class Rede(db.Model):
    __tablename__ = 'rede'
    rede_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)

    
    def __repr__(self):
        return f'<Rede "{self.name}">'
    
