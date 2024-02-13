from flask import Blueprint

bp = Blueprint('Manager', __name__)

from app.manager import routes