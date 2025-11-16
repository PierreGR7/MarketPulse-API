# This file initializes the Flask application
# Import the Flask class and create the application
# Register the market_bp blueprint and return the app

import logging
from flask import Flask, request
from time import time

from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # --- LOGGING CONFIG ---
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    # Log every request
    @app.before_request
    def before_request():
        request.start_time = time()
        app.logger.info(f"➡️  {request.method} {request.path}")

    @app.after_request
    def after_request(response):
        duration = round((time() - request.start_time) * 1000, 2)
        app.logger.info(
            f"⬅️  {request.method} {request.path} [{response.status_code}] - {duration} ms"
        )
        return response

    @app.errorhandler(Exception)
    def handle_error(e):
        app.logger.error(f"!!! ERROR on {request.path}: {str(e)}")
        return {"error": "Internal Server Error"}, 500

    # Register routes
    from .routes import market_bp
    app.register_blueprint(market_bp, url_prefix="/marketpulse")

    return app

