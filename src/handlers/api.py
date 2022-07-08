import logging
from fastapi import APIRouter


logger = logging.getLogger(__name__)
api_router = APIRouter()

# http://localhost:8001/api/hello
@api_router.get("/hello")
def read_root():
    logger.info('getting hello world')
    return {"Hello": "World"}
