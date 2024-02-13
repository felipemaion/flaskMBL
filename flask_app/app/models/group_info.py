from app.extensions import db

class GroupInfo(db.Model):
    group_info_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<GroupInfo "{self.title}">'