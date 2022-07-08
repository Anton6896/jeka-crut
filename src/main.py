import logging
import os
import uvicorn
from fastapi import FastAPI

from src.settings import settings
from src.routers import router
from src.handlers.db_speker import DBConnector

settings.init_logger()
logger = logging.getLogger(__name__)
logger.info('hi jeka i am started')

app = FastAPI()
app.include_router(router)
DBConnector()


def main():
    uvicorn.run('main:app',
                host='0.0.0.0',
                port=settings.APP_PORT,
                reload=True,
                reload_dirs=[os.path.dirname(__file__)])


if __name__ == '__main__':
    main()
