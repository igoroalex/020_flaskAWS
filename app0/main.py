"""
Create Flask server instance, primary app setup
"""
from flask import Flask


def create_app():
    """Primary setup of app"""
    app = Flask(__name__)

    from app.users.users import bp

    app.register_blueprint(bp)

    return app
