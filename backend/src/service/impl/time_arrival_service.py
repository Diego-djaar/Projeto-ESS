from src.schemas.provisory_schemas import Supplier, Product, PreOrder, Order, User
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.time_arrival_response import HTTPTimeArrivalResponse

class TimeArrivalService:

    @staticmethod
    def calculating_time_arrival(product_id: Product.id, user_CPF: User.cpf) -> HttpResponseModel:

        success, data  = calculate_time_arrival_db(product_id, user_CPF)

        if success:
            return HTTPTimeArrivalResponse.GET_SUCESSFULLY(data)
        else:
            return HTTPTimeArrivalResponse.BAD_REQUEST(data)