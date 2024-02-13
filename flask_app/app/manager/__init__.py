from flask import Blueprint

bp = Blueprint('manager', __name__)

from app.manager import routes