# MarketPulse-API
This project is a small financial micro-service built with Flask, Python, and Docker.
It exposes real-time market indicators through a simple REST API.

1. run.py :
It starts the Flask server.
When you run python run.py, it loads the app and exposes the API on port 5000.

2. app/
    - __init__.py : Creates the Flask application and registers the routes using a Blueprint

    - routes.py : Defines the /marketpulse/latest endpoint. When this endpoint is called, it asks   the service layer to fetch the market data

    - services/market_service.py : Contains all the functions that fetch data
        - EUR/USD exchange rate
        - CAC40 index
        - Bitcoin price
        Everything is aggregated into a JSON

3. requirements.txt :
All the librairies used in the project (Flask, yfinance, requests)
They are installed automatically when building the Docker image

4. Dockerfile :
It describes how ti run the API inside a container :
- install python
- install dependencies (requirements.txt)
- copy the code source
- expose port 5000
- start the server

5. docker-compose.yml :
Runs the API with "docker compose up --build" this launches the service on http://localhost:5000/marketpulse/latest

6. tests/
Unit tests for the routes and services

