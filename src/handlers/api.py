import json
import logging
from fastapi import APIRouter
from src.handlers.models import User
from src.handlers.db_speker import DBConnector

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
def create_user(user: User):
    logger.info(f'creating new user, \n{json.dumps(user.serialize(), indent=2)}')
    res = DBConnector().table_insert(user.serialize(), user.get_table_name())
    if res:
        return {'msg': f'user {user.username} created index: {res}'}

    return {'error': f'not created'}


@api_router.patch('/user')
def update_user():
    logger.info('getting hello world')
    return {'msg': 'updating user'}
