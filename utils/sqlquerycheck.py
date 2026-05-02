from config.db_config import get_connection
from utils.logger import get_logger

logger = get_logger()

def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()

    logger.info("Executing query")
    logger.info(f"Query: {query}")

    cursor.execute(query)
    data = cursor.fetchall()

    logger.info(f"Rows returned: {len(data)}")

    cursor.close()
    conn.close()

    return data