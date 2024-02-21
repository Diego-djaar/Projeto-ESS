from fastapi import APIRouter
from src.api import carrinho, users, recuperation, stores, cancel_orders, estimated_time_arrival

api_router = APIRouter()

api_router.include_router(carrinho.router, prefix="/carrinho", tags = ["carrinho"])
api_router.include_router(users.router, prefix="/auth/user", tags = ["user"])
api_router.include_router(recuperation.router, prefix="/esqueciasenha", tags = ["recuperation"])

api_router.include_router(stores.router, prefix="/stores")
api_router.include_router(estimated_time_arrival.router, prefix="/estimated_time_arrival", tags=["Estimated time arrival"])
api_router.include_router(cancel_orders.router, prefix="/orders", tags=["Orders"])