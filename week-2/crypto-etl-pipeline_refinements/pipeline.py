# pipeline.py ETL Pipeline Orchestration
from datetime import datetime
from logger import setup_logger
from extract import extract
from transform import transform
from load import load

logger = setup_logger('Pipeline')

def run_pipeline():
    """
    Execute complete ETL pipeline
    """

    start_time = datetime.now()
    logger.info("=" * 70)
    logger.info("CRYPTO PRICE TRACKER ETL PIPELINE")
    logger.info(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 70)

    try:
        # Extract
        logger.info("\n[1/3] EXTRACT PHASE")
        raw_data = extract()

        # Transform
        logger.info("\n[2/3] TRANSFORM PHASE")
        df = transform(raw_data)

        #Load
        logger.info("\n[3/3] LOAD PHASE")
        records_loaded = load(df)

        #Success summary
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        logger.info("\n" + "=" * 70)
        logger.info("✅ PIPELINE COMPLETED SUCCESSFULLY")
        logger.info("=" * 70)
        logger.info(f"Records processed: {records_loaded}")
        logger.info(f"Duration: {duration:.2f} seconds")
        logger.info(f"Finished at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("=" * 70)

        return True
    
    except Exception as e:
        logger.error("\n" + "=" * 70)
        logger.error("❌ PIPELINE FAILED")
        logger.error("=" * 70)
        logger.error(f"Error: {str(e)}")
        logger.error("=" * 70)
        return False
    
if __name__ == "__main__":
    run_pipeline()