from src.schemas.provisory_schemas import Product, Order, User
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.orders_response import HTTPOrdersResponse
from src.db.orders_db import cancel_order_db

class OrdersService:

    @staticmethod
    def cancel_order_service(product_id: int, user_CPF: str, cancel_reason: str) -> HttpResponseModel:

        success, data  = cancel_order_db(product_id, user_CPF, cancel_reason)

        if success:
            return HTTPOrdersResponse.CANCEL_SUCESSFULLY()
        else:
            return HTTPOrdersResponse.BAD_REQUEST(data)
    
    @staticmethod
    def get_all_orders_service() -> HttpResponseModel:
        pass