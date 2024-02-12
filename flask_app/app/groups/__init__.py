from flask import Blueprint

bp = Blueprint('Group', __name__)

from app.groups import routes