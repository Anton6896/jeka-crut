import logging
from fastapi import APIRouter

logger = logging.getLogger(__name__)
api_router = APIRouter()


# http://localhost:8001/api/user


@api_router.get('/user')
def get_users():
    logger.info('getting hello world')
    return {'msg': 'get_users'}


@api_router.get('/user/{name}')
def get_user(name: str):
    logger.info('getting hello world')
    return {'msg': f'get user {name}'}


@api_router.post('/user')
def create_user():
    logger.info('getting hello world')
    return {'msg': 'creating user'}


@api_router.patch('/user')
def update_user():
    logger.info('getting hello world')
    return {'msg': 'updating user'}
