import logging
import os
import uvicorn
from fastapi import FastAPI

from src.settings import update_logging
from src.settings import settings
from src.routers import router
from src.handlers.db_speker import DBConnector

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(router)


def main():
    logger.info('hi jeka i am started')
    update_logging()
    DBConnector()
    uvicorn.run('main:app',
                host='0.0.0.0',
                port=settings.APP_PORT,
                reload=True,
                reload_dirs=[os.path.dirname(__file__)])


if __name__ == '__main__':
    main()
