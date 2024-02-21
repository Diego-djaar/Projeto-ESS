from fastapi import APIRouter
from src.api import items, order_history

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(order_history.router, prefix="/Orders", tags=["orders"])