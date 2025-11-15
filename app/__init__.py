# This file initializes the Flask application
# Import the Flask class and create the application
# Register the market_bp blueprint and return the app

from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import market_bp
    app.register_blueprint(market_bp, url_prefix="/marketpulse")

    return app
