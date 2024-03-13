from fastapi import APIRouter, status, HTTPException, Response
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.provisory_schemas import Product, Order, User
from fastapi.responses import JSONResponse
from src.service.impl.orders_service import OrdersService


router = APIRouter()

@router.put(
    '/cancel/{id_product}',
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Order cancel by its ID",
    )
def cancel_order(id_product: int, user_CPF: str, cancel_reason:str, response:Response) -> HttpResponseModel:
    request_response = OrdersService.cancel_order_service(id_product, user_CPF, cancel_reason)
    response.status_code = request_response.status_code

    return request_response

@router.get(
    '/get_all',
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Get all cancel products",
    )
def get_all_canceled_orders(user_CPF: str) -> HttpResponseModel:
    response = OrdersService.get_all_orders_service(user_CPF)
    return response

#@router.post(
#    '/create/{id_product}',
#    response_model=HttpResponseModel,
#    status_code=status.HTTP_201_CREATED,
#    description="Create a order from the product in the cart by its ID",
#    )
# def create_order(product_id: int, user_CPF: str) -> HttpResponseModel:
#    pass