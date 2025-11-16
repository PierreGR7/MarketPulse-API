# This file contains all business logic for fetching financial data

import yfinance as yf
import requests
from typing import Optional, Dict, Any, List


def get_eur_usd() -> Optional[float]:
    """Fetch the EUR/USD exchange rate from a public API."""
    url = "https://open.er-api.com/v6/latest/EUR"
    response = requests.get(url).json()

    if "rates" in response and "USD" in response["rates"]:
        return float(response["rates"]["USD"])
    return None


def get_index(symbol: str) -> Optional[float]:
    """Return the latest closing price of a financial index or asset."""
    try:
        ticker = yf.Ticker(symbol)
        history = ticker.history(period="1d")
        return round(float(history["Close"].iloc[-1]), 2)
    except Exception:
        return None

def get_btc_eur() -> Optional[float]:
    """Fetch BTC/EUR price from CoinGecko API"""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"
    try:
        response = requests.get(url).json()
        return float(response["bitcoin"]["eur"])
    except Exception:
        return None



def get_market_data() -> Dict[str, Optional[float]]:
    """Return all market indicators as a dictionary"""
    return {
        "EUR/USD": get_eur_usd(),
        "CAC40": get_index("^FCHI"),
        "BTC/EUR": get_btc_eur()
    }

def get_history_data(symbol: str, period: str = "1mo") -> List[Dict[str, Any]]:
    """
    Fetch historical data using yfinance.
    Returns a list of {"date": "YYYY-MM-DD", "close": float}
    """
    yf_symbol_map = {
        "CAC40": "^FCHI",
        "BTC_EUR": "BTC-EUR",
        "EUR_USD": "EURUSD=X",
    }

    yf_symbol = yf_symbol_map.get(symbol.upper())
    if yf_symbol is None:
        return []

    try:
        ticker = yf.Ticker(yf_symbol)
        hist = ticker.history(period=period)

        points = []
        for index, row in hist.iterrows():
            points.append({
                "date": index.strftime("%Y-%m-%d"),
                "close": round(float(row["Close"]), 2)
            })

        return points
    except Exception:
        return []
