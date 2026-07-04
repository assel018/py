import psycopg2
from config import DB_CONFIG
from loguru import logger


def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.OperationalError as e:
        logger.error(e)
        raise

get_connection()