from src.db.payment_database import Adicionar_cartao
from src.schemas.payment_schema import Cartao
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.payment_response import HTTPPaymentResponse

class PaymentService:

    @staticmethod
    def inserting_method(cartao: Cartao) -> HttpResponseModel:

        sucesso, problemas = Adicionar_cartao(*cartao.model_dump().values())

        if sucesso: 
            return HTTPPaymentResponse.INSERTION_SUCESSFULLY()
        elif "CPF" in problemas or "VALIDADE" in problemas or "CARD_NUMBER" in problemas: 
            return HTTPPaymentResponse.BAD_REQUEST(problemas)
        # elif "VALIDADE" in problemas:
        #     return HTTPPaymentResponse.EXPIRED_DATA()
        # elif "CARD_NUMBER" in problemas:
        #     return HTTPPaymentResponse.INVALID_NUMBER()
