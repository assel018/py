import psycopg2
from loguru import logger
from config import DB_CONFIG


def get_connection():
    """
    Create and return a connection to the PostgreSQL database.
    """

    try:
        return psycopg2.connect(**DB_CONFIG)

    except psycopg2.OperationalError as error:
        logger.error(f"Database connection failed: {error}")
        raise