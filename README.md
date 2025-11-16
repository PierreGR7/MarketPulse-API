# MarketPulse API

A small Flask API that provides live market indicators (EUR/USD, CAC40, BTC/EUR), historical data, and a minimal dashboard built with Bootstrap and Chart.js.
The project is fully dockerized and designed with a simple modular structure.

## Features

Live market data (JSON)

Historical price data (JSON)

Dashboard UI (HTML)

History viewer with charts (HTML)

Config endpoint

Development + production Docker setup

## Project Structure

app/
├── __init__.py          # Flask app factory + logging
├── routes.py            # Routes (JSON + HTML)
├── config.py            
├── services/
│   └── market_service.py  # Data fetching with yfinance, requests, coingecko
└── templates/           # HTML pages (home, dashboard, history, navigation_home)
run.py
Dockerfile
docker-compose.yml # Development
docker-compose.prod.yml
requirements.txt

## Key Endpoints

### JSON

/marketpulse/latest

/marketpulse/history

/marketpulse/config

### HTML

/marketpulse/

/marketpulse/dashboard

/marketpulse/history/view

# HOW TO RUN

## Run With Docker

### Development
docker compose up --build

### Production
docker compose -f docker-compose.prod.yml up --build

## Run Without Docker

pip install -r requirements.txt

python run.py

## Example (Latest Data)
{
  "timestamp": "2025-11-16T13:04:10Z",
  "data": {
    "EUR/USD": 1.07,
    "CAC40": 7150.09,
    "BTC/EUR": 68000.12
  }
}
