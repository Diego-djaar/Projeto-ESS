from fastapi import APIRouter
from src.api import carrinho, users, recuperation

api_router = APIRouter()

api_router.include_router(carrinho.router, prefix="/carrinho", tags = ["carrinho"])
api_router.include_router(users.router, prefix="/auth/user", tags = ["user"])
api_router.include_router(recuperation.router, prefix="/esqueciasenha", tags = ["recuperation"])
