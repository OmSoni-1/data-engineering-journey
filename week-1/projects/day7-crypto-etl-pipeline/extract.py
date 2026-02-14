# extract.py - Data extraction from CoinGecko API
import requests
from logger import setup_logger
from config import Config

logger = setup_logger('Extract')

def fetch_crypto_prices():
    """
    Fetch cryptocurrency prices from CoinGecko API
    Returns: Dictionary with crypto data.
    """
    logger.info("Starting data extraction from CoinGeclo API")

    # Build API endpoint
    crypto_ids = ','.join(Config.CRYPTO_IDS)
    url = f"{Config.API_BASE_URL}/simple/price"

    params = {
        'ids': crypto_ids,
        'vs_currencies': Config.VS_CURRENCY,
        'include_24hr_change': 'true',
        'include_market_cap': 'true',
        'include_24hr_vol': 'true'
    }

    logger.debug(f"API URL: {url}")
    logger.debug(f"Parameters: {params}")

    try:
        # Make API request
        logger.info(f"Fetching data for: {Config.CRYPTO_IDS}")
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        logger.info(f"✓ Successfully fetched data for {len(data)} cryptocurrencies")
        logger.debug(f"Raw response: {data}")

        return data
    
    except requests.exceptions.Timeout:
        logger.error("API request timed out")
        raise
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during execution: {e}")
        raise

def extract():
    """Main extract function"""
    logger.info("=" * 60)
    logger.info("Extract Phase - Starting...")
    logger.info("=" * 60)

    try:
        data = fetch_crypto_prices()
        logger.info("✓ Extract phase completed successfully")
        return data
    
    except Exception as e:
        logger.error("x Extract phase failed: {e}")
        raise

if __name__ == "__main__":
    result = extract()
    print("\n ✓ Extracted Data:")
    for crypto, values in result.items():
        print(f" {crypto}: ₹{values.get('inr', 'N/A')}")