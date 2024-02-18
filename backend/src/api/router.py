from fastapi import APIRouter
from src.api import users, recuperation, payment_methods

api_router = APIRouter()
# api_router.include_router(items.router, prefix="/items", tags=["items"])

api_router.include_router(users.router, prefix="/auth/user", tags = ["user"])
api_router.include_router(recuperation.router, prefix="/esqueciasenha", tags = ["recuperation"])
api_router.include_router(payment_methods.router, prefix="/payment", tags=["Payment"])