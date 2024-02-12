from flask import jsonify, url_for, redirect
from app.helper import auth
from app.login import bp


@bp.route("/", methods=["POST"])
def authenticate():
    return auth()
