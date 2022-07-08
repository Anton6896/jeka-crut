from fastapi import APIRouter

from src.handlers.api import api_router

router = APIRouter()

router.include_router(api_router, prefix='/api')
