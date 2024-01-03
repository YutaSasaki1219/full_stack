from fastapi import APIRouter

api_router = APIRouter()

from app.api.endpoints import hello

api_router = APIRouter()
api_router.include_router(hello.router, prefix="", tags=["hello"])