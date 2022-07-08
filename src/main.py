import logging
import os
from typing import Union
import uvicorn
from fastapi import FastAPI
from settings import update_logging

from settings import settings

logger = logging.getLogger(__name__)

app = FastAPI()


def main():
    logger.info('hi jeka i am started')
    update_logging()
    


    uvicorn.run('main:app',
                host='0.0.0.0',
                port=settings.APP_PORT,
                reload=True,
                reload_dirs=[os.path.dirname(__file__)])



@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    main()