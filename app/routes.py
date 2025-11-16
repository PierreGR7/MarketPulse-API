# This file defines the HTTP routes of the API
# Import the Blueprint class and the get_market_data function
# Create a Blueprint object for the market routes
# Define the latest_data route that returns the latest market data

from flask import Blueprint, jsonify, render_template, request, current_app
from .services.market_service import get_market_data, get_history_data
from datetime import datetime, timezone

market_bp = Blueprint("market", __name__)

@market_bp.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@market_bp.route("/latest", methods=["GET"])
def latest_data():
    data = get_market_data()
    return jsonify({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "data": data
    })

@market_bp.route("/dashboard", methods=["GET"])
def dashboard_view():
    data = get_market_data()
    return render_template("dashboard.html", data=data)


@market_bp.route("/history", methods=["GET"])
def history():
    symbol = request.args.get("symbol", "CAC40")
    period = request.args.get("period", "1mo")

    data = get_history_data(symbol=symbol, period=period)

    return jsonify({
        "symbol": symbol,
        "period": period,
        "timestamp": datetime.now(timezone.utc).isoformat() + "Z",
        "history": data
    })

@market_bp.route("/history/view", methods=["GET"])
def history_view():
    return render_template("history.html")

@market_bp.route("/config", methods=["GET"])
def config_view():
    cfg = {
        "service": current_app.config["SERVICE_NAME"],
        "version": current_app.config["VERSION"],
        "environment": current_app.config["ENVIRONMENT"],
        "default_period": current_app.config["DEFAULT_PERIOD"],
        "debug": current_app.config["DEBUG"],
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    return jsonify(cfg)
