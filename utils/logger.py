import logging
import os

def create_logger(name):
    #create logs folder if it not exists
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # File handler
    fh = logging.FileHandler("logs/test_run.log", encoding="utf-8")
    fh.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # Add handler to logger
    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger