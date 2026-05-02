import logging
import os

# Ensure reports folder exists
if not os.path.exists("reports"):
    os.makedirs("reports")

def get_logger():
    logger = logging.getLogger("ETL_TEST_LOGGER")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if not logger.handlers:

        # File handler
        file_handler = logging.FileHandler("reports/test_log.log")
        file_handler.setLevel(logging.INFO)

        # Format
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger