import datetime
from functools import wraps

from flask import request, jsonify
from app.models.manager import Manager, Role
import jwt
from werkzeug.security import check_password_hash
from dotenv import dotenv_values

config = dotenv_values(".env")

#### Referencia:
# https://medium.com/@hedgarbezerra35/api-rest-com-flask-autenticacao-25d99b8679b6
# https://github.com/hedgarbezerra/Another-FlaskAPI/blob/master/app/routes/routes.py


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            return jsonify({"message": "token is missing", "data": []}), 401
        try:
            data = jwt.decode(token, config["SECRET_KEY"],algorithms='HS256')
            current_user = Manager.get_by_username(username=data["username"])
        except Exception as e:
            return jsonify({"message": "token is invalid or expired", "data": [str(e)]}), 401
        return f(current_user, *args, **kwargs)

    return decorated


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        current_manager = args[0]
        if current_manager.role == Role.ADMIN:
            return f(*args, **kwargs)
        return jsonify({"message": "You must be ADMIN", "data": []}), 401
    return decorated


def manager_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        current_manager = args[0]
        if current_manager.role == Role.MANAGER or current_manager.role == Role.ADMIN:
            return f(*args, **kwargs)
        return jsonify({"message": "You must be ADMIN", "data": []}), 401
    return decorated


def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return (jsonify({
                    "message": "could not verify",
                    "WWW-Authenticate": 'Basic auth="Login required"',
                }), 401)
    user = Manager.get_by_username(auth.username)
    if not user:
        return jsonify({"message": "user not found", "data": []}), 401
    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode(
            {
                "username": user.user_name,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=12),
            },
            config["SECRET_KEY"],
            algorithm='HS256'
        )
        return jsonify(
            {
                "message": "Validated successfully",
                "token": token,  # .decode("UTF-8"),
                "exp": datetime.datetime.now() + datetime.timedelta(hours=12),
            }
        )
    return (jsonify({
                "message": "could not verify",
                "WWW-Authenticate": 'Basic auth="Login required"',
            }), 401)
