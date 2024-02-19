from src.schemas.provisory_schemas import Product, Order, User
from src.schemas.history import OrderFilter
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.orders_response import HTTPOrdersResponse
from src.db.orders_db import cancel_order_db, get_all_orders_db, orders_user, order_user, orders_filtered

class OrdersService:

    @staticmethod
    def cancel_order_service(product_id: int, user_CPF: str, cancel_reason: str) -> HttpResponseModel:

        success, data  = cancel_order_db(product_id, user_CPF, cancel_reason)

        if success:
            return HTTPOrdersResponse.CANCEL_SUCCESSFULLY()
        else:
            return HTTPOrdersResponse.BAD_REQUEST(data)
    
    @staticmethod
    def get_all_orders_service(user_CPF: str) -> HttpResponseModel:
        
        success, data = get_all_orders_db(user_CPF)

        if success:
            return HTTPOrdersResponse.GET_SUCCESSFULLY(data)
        else:
            return HTTPOrdersResponse.NO_CANCEL_ORDERS()
        
    @staticmethod
    def orders_user_service(user_CPF: str) -> HttpResponseModel:
        data = orders_user(user_CPF)
        return HTTPOrdersResponse.GET_SUCCESSFULLY(data)
    
    @staticmethod
    def order_user_service(user_CPF: str, order_id: int) -> HttpResponseModel:
        data = order_user(user_CPF, order_id)
        return HTTPOrdersResponse.USER_ORDER(data)
    
    @staticmethod
    def orders_filtered_service(filter: OrderFilter) -> HttpResponseModel:
        data = orders_filtered(filter)
        return HTTPOrdersResponse.GET_SUCCESSFULLY(data)