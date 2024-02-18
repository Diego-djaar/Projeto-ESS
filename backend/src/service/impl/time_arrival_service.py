from src.schemas.provisory_schemas import Supplier, Product, Order, User
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.time_arrival_response import HTTPTimeArrivalResponse
from src.db.time_arrival_db import calculate_time_arrival_db

class TimeArrivalService:

    @staticmethod
    def calculating_time_arrival(product_id: int, user_CPF: str) -> HttpResponseModel:

        success, data  = calculate_time_arrival_db(product_id, user_CPF)

        if success:
            return HTTPTimeArrivalResponse.GET_SUCESSFULLY(data)
        else:
            return HTTPTimeArrivalResponse.BAD_REQUEST(data)