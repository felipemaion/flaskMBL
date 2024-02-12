from flask import Blueprint

bp = Blueprint('Visitor', __name__)

from app.links import routes