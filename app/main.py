"""
Create Flask server instance, primary app setup
"""
from flask import Flask

from config import settings


def create_app():
    """Primary setup of app"""
    app = Flask(__name__)
    app.config.from_object(settings)

    from app.users.users import bp

    app.register_blueprint(bp)

    return app
