import os
from pydantic import BaseSettings
import logging


class Settings(BaseSettings):
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'jekakrut')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'jeka')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', 'krut')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', '5432')

    APP_PORT: int = int(os.getenv('APP_PORT', '8001'))

    def db_params(self):
        return {
            'database': self.POSTGRES_DB,
            'user': self.POSTGRES_USER,
            'password': self.POSTGRES_PASSWORD,
            'host': self.POSTGRES_HOST,
            'port': self.POSTGRES_PORT
        }

    def init_logger(self):
        logging.basicConfig(
            format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d:%H:%M:%S',
            level=logging.DEBUG
        )


settings = Settings()
