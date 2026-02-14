# config.py - Centralized configuration management
import os
from dotenv import load_dotenv

# To load the environment variables
load_dotenv()

class Config:
    """Application configuration"""

    # Database settings
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'crypto_tracker')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    # API SETTINGS
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.coingecko.com/api/v3')

    # Cryptocurrencies to track
    CRYPTO_IDS = ['bitcoin', 'ethereum', 'cardano', 'solana', 'ripple']

    # Target Currency
    VS_CURRENCY = 'inr'

    @classmethod
    def get_db_connection_string(cls):
        """Get PostgreSQL connection string"""
        return f"postgresql://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
    
    @classmethod
    def validate(cls):
        """Validate Configuration"""
        if not cls.DB_PASSWORD:
            raise ValueError("DB_PASSWORD not set in .env file")
        return True
    
# Validate config on import    
Config.validate() 