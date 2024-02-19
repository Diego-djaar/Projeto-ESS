from fastapi import APIRouter
from src.api import users, recuperation, payment_methods
from src.api import carrinho

api_router = APIRouter()

api_router.include_router(users.router, prefix="/auth/user", tags = ["user"])

api_router.include_router(carrinho.router, prefix="/carrinho", tags = ["carrinho"])
api_router.include_router(recuperation.router, prefix="/esqueciasenha", tags = ["recuperation"])
api_router.include_router(payment_methods.router, prefix="/payment", tags=["Payment"])