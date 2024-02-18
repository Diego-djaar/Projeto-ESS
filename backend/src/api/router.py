from fastapi import APIRouter
from src.api import users, recuperation

api_router = APIRouter()

api_router.include_router(users.router, prefix="/auth/user", tags = ["user"])
api_router.include_router(recuperation.router, prefix="/esqueciasenha", tags = ["recuperation"])