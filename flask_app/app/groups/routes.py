from app.groups import bp
from app.extensions import db
from app.models.group import Group

@bp.route('/')
def index():
    posts = Group.query.all()
    return posts