from flask import Blueprint

bp = Blueprint('rede', __name__)

from app.rede import routes