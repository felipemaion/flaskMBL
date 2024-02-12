from app.groups import bp
from app.extensions import db
from app.models.group import Group
from app import helper

@bp.route('/')
@helper.token_required
def index(current_manager):
    posts = Group.query.all()
    return posts