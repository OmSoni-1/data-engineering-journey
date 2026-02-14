import pandas as pd
from datetime import datetime
from logger import setup_logger
from config import Config

logger = setup_logger('Transform')

def transform_crypto_data(raw_data):
    """
    Transform raw API data into structured DataFrame
    """

    logger.info("Starting data transformation")

    transformed_records = []
    timestamp = datetime.now()

    for crypto_id, values in raw_data.items():
        try:
            # Extract values with default
            price = values.get(Config.VS_CURRENCY.lower(), None)
            market_cap = values.get(f"{Config.VS_CURRENCY.lower()}_market_cap", None)
            volume_24h = values.get(f"{Config.VS_CURRENCY.lower()}_24h_vol", None)
            change_24h = values.get(f"{Config.VS_CURRENCY.lower()}_24h_change", None)

            # Create record
            record = {
                'crypto_id': crypto_id,
                'crypto_name': crypto_id.replace('-', ' ').title(),
                'price_inr': price,
                'market_cap_inr': market_cap,
                'volume_24h_inr': volume_24h,
                'price_change_24h_pct': change_24h,
                'extracted_at': timestamp,
                'is_positive_change': change_24h > 0 if change_24h else None
            }

            transformed_records.append(record)
            logger.debug(f"Transformed {crypto_id}: ₹{price}")

        except Exception as e:
            logger.warning(f"Error transforming {crypto_id}: {e}")
            continue

    # Create DataFrame
    df = pd.DataFrame(transformed_records)

    # Add calculated columns
    if not df.empty:
        # Price category
        df['price_category'] = df['price_inr'].apply(
            lambda x: 'High' if x > 90000 else ('Medium' if x > 9000 else 'Low')
        )

        # Round numeric values
        df['price_inr'] = df['price_inr'].round(2)
        df['price_change_24h_pct'] = df['price_change_24h_pct'].round(2)  
        df['volume_24h_inr'] = df['volume_24h_inr'].round(2)
        df['market_cap_inr'] = df['market_cap_inr'].round(2)

        logger.info(f"✓ Transformed {len(df)} records")
        logger.debug(f"Columns: {list(df.columns)}")
    else:
        logger.warning("No records to transform!")

    return df

def transform(raw_data):
    """Main transform function"""
    logger.info("=" * 60)
    logger.info("TRANSFORM PHASE - STARTING...")
    logger.info("=" * 60)

    try:
        df = transform_crypto_data(raw_data)

        # Data quality checks
        logger.info("Running data quality checks...")

        # Check for nulls
        null_counts = df.isnull().sum()
        if null_counts.any():
            logger.warning(f"Null values found:\n{null_counts[null_counts > 0]}")

        # Summary stats
        logger.info(f"Price range: ₹{df['price_inr'].min():.2f} - ₹{df['price_inr'].max():.2f}")
        positive_changes = df['is_positive_change'].sum()
        logger.info(f"Positive changes: {positive_changes} / {len(df)}")

        logger.info("✓ Transform phase completed successfully")
        return df
    
    except Exception as e:
        logger.error("x Transform Phase failed")
        raise

if __name__ == "__main__":
    # Test transformation
    from extract import extract

    raw_data = extract()
    df = transform(raw_data)
    print("\n✓ Transformed Data:")
    print(df.to_string())