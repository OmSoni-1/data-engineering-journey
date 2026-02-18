# Logger.py - Logging setup
import logging
import os
from datetime import datetime

def setup_logger(name='CryptoETL'):
    """Setup logger with console and file handlers"""

    # Create logs directory
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Logger setup
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.handlers = []

    # Console handler (INFO level)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console_format = logging.Formatter('%(levelname)s - %(message)s')
    console.setFormatter(console_format)

    # File handler (DEBUG level)
    log_file = f"logs/pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_format)

    # Add handlers
    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger