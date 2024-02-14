from src.db.payment_database import Adicionar_cartao
from src.schemas.payment_schema import Cartao
from src.schemas.response import HTTPResponses, HttpResponseModel

class PaymentService:

    @staticmethod
    def inserting_method(cartao: Cartao) -> HttpResponseModel:

        consulta = Adicionar_cartao(*cartao.model_dump().values())

        if consulta: 
            return HTTPResponses.ITEM_CREATED
