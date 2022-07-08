import logging
import psycopg2

from src.settings import settings

logger = logging.getLogger(__name__)


class DBConnector:
    def __init__(self) -> None:
        self.connection = None
        self.ensure_tables()

    def get_connection(self):
        logger.info('getting connection')

        if self.connection:
            return self.connection

        self.connection = psycopg2.connect(**settings.db_params())
        return self.connection

    def ensure_tables(self):
        logger.info('ensuring tables')

    def __del__(self):
        if self.connection:
            logger.info('closing unclosed connection')
            self.connection.close()
