from flask import Blueprint

bp = Blueprint('Influencer', __name__)

from app.influencer import routes