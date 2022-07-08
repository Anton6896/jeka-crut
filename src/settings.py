import logging.config
import os
from pydantic import BaseSettings


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


def update_logging():
    from uvicorn.config import LOGGING_CONFIG

    LOGGING_CONFIG['formatters']['default']['fmt'] = \
        '%(asctime)s [%(name)14s] %(levelprefix)s %(message)s'
    LOGGING_CONFIG['formatters']['access']['fmt'] = \
        '%(asctime)s [%(name)14s] %(levelprefix)s %(client_addr)s - \'%(request_line)s\' %(status_code)s'
    LOGGING_CONFIG['loggers']['storer'] = {
        'handlers': ['default'],
        'formatter': 'default',
        'level': 'DEBUG',
        'propagate': True
    }
    logging.config.dictConfig(LOGGING_CONFIG)


settings = Settings()
