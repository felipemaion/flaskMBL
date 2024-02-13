from flask_cors import cross_origin
from app.helper import auth
from app.login import bp


@bp.route("/", methods=["POST"])
@cross_origin()
def authenticate():
    return auth()
