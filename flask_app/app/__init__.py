from flask import Flask
from flask_cors import CORS
from config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    # cors = CORS(app, resources={r"/*": {"origins": "*"}})
    cors = CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}})
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.groups import bp as groups_bp

    app.register_blueprint(groups_bp, url_prefix="/groups")

    from app.influencer import bp as influencer_bp

    app.register_blueprint(influencer_bp, url_prefix="/influencer")

    from app.links import bp as links_bp

    app.register_blueprint(links_bp, url_prefix="/links")

    from app.manager import bp as manager_bp

    app.register_blueprint(manager_bp, url_prefix="/manager")

    from app.visitor import bp as visitor_bp

    app.register_blueprint(visitor_bp, url_prefix="/visitor")

    from app.login import bp as login_bp

    app.register_blueprint(login_bp, url_prefix="/login")

    @app.route("/")
    def test_page():
        return ""

    return app
