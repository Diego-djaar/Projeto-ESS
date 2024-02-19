from fastapi import APIRouter
from src.api import users
from src.api import carrinho

api_router = APIRouter()

api_router.include_router(users.router, prefix="/auth/user", tags = ["user"])

api_router.include_router(carrinho.router, prefix="/carrinho", tags = ["carrinho"])