from flask import Blueprint

bp = Blueprint('Link', __name__)

from app.links import routes