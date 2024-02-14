from src.db.payment_database import Adicionar_cartao, Adicionar_pix, Adicionar_boleto
from src.schemas.payment_schema import Cartao, Pix, Boleto 
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.payment_response import HTTPPaymentResponse

class PaymentService:

    @staticmethod
    def inserting_cartao(cartao: Cartao) -> HttpResponseModel:

        sucesso, problemas = Adicionar_cartao(*cartao.model_dump().values())

        if sucesso: 
            return HTTPPaymentResponse.INSERTION_SUCESSFULLY()
        elif "CPF" in problemas or "VALIDADE" in problemas or "CARD_NUMBER" in problemas: 
            return HTTPPaymentResponse.BAD_REQUEST(problemas)
        # elif "VALIDADE" in problemas:
        #     return HTTPPaymentResponse.EXPIRED_DATA()
        # elif "CARD_NUMBER" in problemas:
        #     return HTTPPaymentResponse.INVALID_NUMBER()
    
    @staticmethod
    def insertion_pix(pix: Pix) -> HttpResponseModel: 

        Adicionar_pix(*pix.model_dump().values())

        return HTTPPaymentResponse.PIX_INSERTED_SUCESSFULLY()
    
    @staticmethod
    def insertion_boleto(boleto: Boleto) -> HttpResponseModel: 

        Adicionar_boleto(*boleto.model_dump().values())

        return HTTPPaymentResponse.BOLETO_INSERTED_SUCESSFULLY()
