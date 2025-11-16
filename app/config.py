import os

class Config:
    SERVICE_NAME = "MarketPulse API"
    VERSION = "1.0.0"

    # Environment : development / production
    ENVIRONMENT = os.getenv("APP_ENV", "development")

    # Default period for history
    DEFAULT_PERIOD = os.getenv("DEFAULT_PERIOD", "1mo")

    # Debug mode
    DEBUG = os.getenv("DEBUG", "True") == "True"
