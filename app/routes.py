# This file defines the HTTP routes of the API
# Import the Blueprint class and the get_market_data function
# Create a Blueprint object for the market routes
# Define the latest_data route that returns the latest market data

from flask import Blueprint, jsonify, render_template
from .services.market_service import get_market_data

market_bp = Blueprint("market", __name__)

@market_bp.route("/latest", methods=["GET"])
def latest_data():
    """Return the latest market data (EUR/USD, CAC40, BTC/EUR)."""
    data = get_market_data()
    return render_template("dashboard.html", data=data)

