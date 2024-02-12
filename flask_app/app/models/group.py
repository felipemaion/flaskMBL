from app.extensions import db

class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    group_info_id = db.Column(db.Integer, db.ForeignKey('group_info.group_info_id'))
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.influencer_id'))
    link_id = db.Column(db.Integer, db.ForeignKey('link.link_id'))


    def __repr__(self):
        return f'<Groups "{self.group_id}">'