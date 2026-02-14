import psycopg2
from psycopg2 import Error
from logger import setup_logger
from config import Config

logger = setup_logger('Load')

def get_db_connection():
    """Create PostgreSQL connection"""
    try:
        connection = psycopg2.connect(
            host = Config.DB_HOST,
            port = Config.DB_PORT,
            database = Config.DB_NAME,
            user = Config.DB_USER,
            password = Config.DB_PASSWORD
        )
        logger.debug("Database connection established")
        return connection
    except Error as e:
        logger.error(f"Error connecting to database: {e}")
        raise

def load_to_postgres(df):
    """
    Load DataFrame to PostgreSQL
    """
    logger.info(f"Loading {len(df)} records to PostgreSQL")

    connection = None
    cursor = None

    try:
        # Connect to Database
        connection = get_db_connection()
        cursor = connection.cursor()

        #Prepare insert query
        insert_query = """
        INSERT INTO crypto_prices (
            crypto_id, crypto_name, price_inr, market_cap_inr, volume_24h_inr, price_change_24h_pct,
            price_category, is_positive_change, extracted_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
        
        # Insert each record
        records_inserted = 0
        for _, row in df.iterrows():
            try:
                cursor.execute(insert_query, (
                    row['crypto_id'],
                    row['crypto_name'],
                    row['price_inr'],
                    row['market_cap_inr'],
                    row['volume_24h_inr'],
                    row['price_change_24h_pct'],
                    row['price_category'],
                    row['is_positive_change'],
                    row['extracted_at']
                ))
                records_inserted += 1
                logger.debug(f"Inserted: {row['crypto_name']}:")
            
            except Error as e:
                logger.warning(f"Error inserting {row['crypto_name']}: {e}")
                continue

            # Commit transaction
            connection.commit()
            logger.info(f"✓ Successfully loaded {records_inserted} records")

            # Verify insert
            cursor.execute("SELECT COUNT(*) from crypto_prices")
            total_records = cursor.fetchone()[0]
            logger.info(f"Total records in database: {total_records}")

            return records_inserted
    
    except Error as e:
        if connection:
            connection.rollback()
        logger.error(f"Database error: {e}")
        raise

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            logger.debug("Database connection closed")

def load(df):
    """Main load function"""
    logger.info("=" * 60)
    logger.info("LOAD PHASE - Starting")
    logger.info("=" * 60)

    try:
        records_inserted = load_to_postgres(df)
        logger.info("✓ Load phase completed successfully")
        return records_inserted
    except Exception as e:
        logger.error("x Load phase failed")
        raise

if __name__ == "__main__":
    #Test loading
    from extract import extract
    from transform import transform

    print("Testing complete ETL chain...\n")
    raw_data = extract()
    df = transform(raw_data)
    load(df)
    print("\n ✓ Data successfully loaded to PostgreSQL!")