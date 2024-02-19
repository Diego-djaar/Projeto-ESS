from fastapi import APIRouter
from src.api import users, payment_methods

api_router = APIRouter()


api_router.include_router(users.router, prefix="/auth/user", tags = ["user"])
api_router.include_router(payment_methods.router, prefix="/payment", tags=["Payment"])