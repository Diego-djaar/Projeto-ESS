from fastapi import APIRouter, status
from src.schemas.response import HttpResponseModel
from src.schemas.history import OrderFilter
from src.db.orders_db import validate_orders
from src.schemas.provisory_schemas import Order
from src.db.orders_db import read_file
from src.service.impl.orders_service import OrdersService

router = APIRouter()

@router.get("/orders_by_user/{user_cpf}", status_code= status.HTTP_200_OK, description = "Get all orders by User CPF", tags=["Orders"], response_model= HttpResponseModel)
def orders_user(user_cpf: str):
    response = OrdersService.orders_user_service(user_cpf)
    return response
    
@router.get("/order_from_user/{user_cpf}&{order_id}", status_code= status.HTTP_200_OK, description = "Get specif order by User CPF and Order Id", tags=["Orders"], response_model= HttpResponseModel)
def orders_user(user_cpf: str, order_id: int):
    response = OrdersService.order_user_service(user_cpf, order_id)
    return response
    
@router.post("/orders_filtered/", status_code= status.HTTP_200_OK, description = "Get filtered order by parameters", tags=["Orders"], response_model= HttpResponseModel)
def orders_filtered(filtro: OrderFilter):
   response = OrdersService.orders_filtered_service(filtro)
   return response 