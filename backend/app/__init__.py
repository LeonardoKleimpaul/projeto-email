from flask import Flask
from app.extensions import db, cors
from flask_cors import CORS
from .routes.email_routes import email_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    cors.init_app(app)

    app.register_blueprint(email_bp, url_prefix='/api/email')

    return app
