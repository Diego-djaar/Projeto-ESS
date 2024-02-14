from fastapi import APIRouter
from src.api import items, payment_methods

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(payment_methods.router, prefix="/backend/src/api/payment", tags=["Payment"])