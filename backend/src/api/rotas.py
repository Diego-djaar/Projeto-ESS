from fastapi import APIRouter

from controllers import store_controller as stores

router = APIRouter()

router.include_router(stores.router, prefix='/stores')