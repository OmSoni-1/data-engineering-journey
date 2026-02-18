# load.py - FIXED VERSION with proper NULL handling
import psycopg2
from psycopg2 import Error
from psycopg2.extras import execute_batch
from logger import setup_logger
from config import Config
import pandas as pd
import time

start_time = time.time()

logger = setup_logger('Load')

def get_db_connection():
    """Create PostgreSQL connection"""
    try:
        connection = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD
        )
        logger.debug("Database connection established")
        return connection
    except Error as e:
        logger.error(f"Error connecting to database: {e}")
        raise

def load_to_postgres(df):
    """
    Load DataFrame to PostgreSQL with proper NULL handling
    """
    logger.info(f"Loading {len(df)} records to PostgreSQL")
    
    connection = None
    cursor = None
    
    try:
        # Connect to database
        connection = get_db_connection()
        cursor = connection.cursor()

        # Create tables if not exists (for containerized DB)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id SERIAL PRIMARY KEY,
            crypto_id VARCHAR(50) NOT NULL,
            crypto_name VARCHAR(100) NOT NULL,
            price_inr DECIMAL(20,2),
            market_cap_inr BIGINT,
            volume_24h_inr BIGINT,
            price_change_24h_pct DECIMAL(10,2),
            price_category VARCHAR(20),
            is_positive_change BOOLEAN,
            extracted_at TIMESTAMP NOT NULL
        );
        """)

        cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS unique_crypto_timestamp
        ON crypto_prices (crypto_id, extracted_at);
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices_latest (
            crypto_id VARCHAR(50) PRIMARY KEY,
            crypto_name VARCHAR(100),
            price_inr DECIMAL(20,2),
            market_cap_inr BIGINT,
            volume_24h_inr BIGINT,
            price_change_24h_pct DECIMAL(10,2),
            price_category VARCHAR(20),
            is_positive_change BOOLEAN,
            extracted_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        
        # Prepare insert query
        insert_query = """
        INSERT INTO crypto_prices (
            crypto_id, crypto_name, price_inr, market_cap_inr,
            volume_24h_inr, price_change_24h_pct, price_category,
            is_positive_change, extracted_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (crypto_id, extracted_at)
        DO NOTHING;
        """

        snapshot_query = """
        INSERT INTO crypto_prices_latest (
            crypto_id, crypto_name, price_inr, market_cap_inr, volume_24h_inr,
            price_change_24h_pct, price_category, is_positive_change, extracted_at
        )
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)

        ON CONFLICT (crypto_id)
        DO UPDATE SET
            crypto_name = EXCLUDED.crypto_name,
            price_inr = EXCLUDED.price_inr,
            market_cap_inr = EXCLUDED.market_cap_inr,
            volume_24h_inr = EXCLUDED.volume_24h_inr,
            price_change_24h_pct = EXCLUDED.price_change_24h_pct,
            price_category = EXCLUDED.price_category,
            is_positive_change = EXCLUDED.is_positive_change,
            extracted_at = EXCLUDED.extracted_at,
            updated_at = CURRENT_TIMESTAMP;
        """
        
        # Track successes and failures
        records_inserted = 0
        
        # ============================================================
        # KEY FIX: Replace pandas NaN with Python None (PostgreSQL NULL)
        # ============================================================
        # Pandas uses NaN for missing values
        # PostgreSQL uses NULL
        # psycopg2 expects Python None for NULL
        # 
        # 
        # ============================================================


        df_clean = df.where(pd.notna(df), None)

        records = [
            (
                row['crypto_id'],
                row['crypto_name'],
                row['price_inr'],
                row['market_cap_inr'],
                row['volume_24h_inr'],
                row['price_change_24h_pct'],
                row['price_category'],
                row['is_positive_change'],
                row['extracted_at']
            )
            for _, row in df_clean.iterrows()
        ]
        
        # Batch insert
        try:
            execute_batch(cursor, insert_query, records, page_size=100)

            execute_batch(cursor, snapshot_query, records, page_size=100)

            connection.commit()

            records_inserted = len(records)


            logger.info(f"✓ {len(records)} processed in batch.)")
            
        except Error as e:
            connection.rollback()
            logger.error("Batch insert failed.")
            logger.error(f"Error: {e}")
            raise
            # Continue to try other records
            
        
        # Verify insert with detailed query
        cursor.execute("""
            SELECT crypto_name, COUNT(*) 
            FROM crypto_prices 
            WHERE extracted_at >= NOW() - INTERVAL '5 minutes'
            GROUP BY crypto_name
            ORDER BY crypto_name
        """)
        recent_inserts = cursor.fetchall()
        
        logger.info(f"="*60)
        logger.info("VERIFICATION - Recent inserts (last 5 mins):")
        logger.info(f"="*60)
        for crypto, count in recent_inserts:
            logger.info(f"  ✓ {crypto}: {count} record(s)")
        
        if len(recent_inserts) < len(df):
            logger.warning(f"Expected {len(df)} cryptos, but only {len(recent_inserts)} were inserted!")
        
        # Total count
        cursor.execute("SELECT COUNT(*) FROM crypto_prices")
        total_records = cursor.fetchone()[0]
        logger.info(f"Total records in database: {total_records}")
        logger.info(f"="*60)
        
        return records_inserted
        
    except Error as e:
        if connection:
            connection.rollback()
            logger.error("Transaction rolled back due to error")
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
    logger.info("="*60)
    logger.info("LOAD PHASE - Starting")
    logger.info("="*60)
    
    try:
        records_inserted = load_to_postgres(df)
        
        if records_inserted == len(df):
            logger.info("✓ Load phase completed successfully - ALL RECORDS INSERTED")
        else:
            logger.warning(f"⚠ Load phase completed with issues - {records_inserted}/{len(df)} records inserted")
        
        return records_inserted
    except Exception as e:
        logger.error("✗ Load phase failed")
        raise

if __name__ == "__main__":
    # Test loading
    from extract import extract
    from transform import transform
    
    print("Testing complete ETL chain...\n")
    raw_data = extract()
    df = transform(raw_data)
    
    print("\nDataFrame to be loaded:")
    print(df.to_string())
    print(f"\nNull values per column:")
    print(df.isnull().sum())
    print()
    
    load(df)
    print("\n✓ Load test complete!")

    end_time = time.time()
    logger.info(f"Load phase took {end_time - start_time: .4f} seconds")