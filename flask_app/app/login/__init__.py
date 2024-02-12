from flask import Blueprint

bp = Blueprint("Login", __name__)

from app.login import routes
