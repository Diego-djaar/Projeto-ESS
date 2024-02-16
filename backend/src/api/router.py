from fastapi import APIRouter
from src.api import items, cancel_orders, estimated_time_arrival

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(estimated_time_arrival.router, prefix="/estimated_time_arrival", tags=["Estimated time arrival"])
api_router.include_router(cancel_orders.router, prefix="/cancel_orders", tags=["Cancel orders"])