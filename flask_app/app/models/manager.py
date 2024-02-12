from app.extensions import db

class Manager(db.Model):
    __tablename__ = 'manager'
    manager_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    password = db.Column(db.String(255))
    
    def __repr__(self):
        return f'<Manager "{self.title}">'