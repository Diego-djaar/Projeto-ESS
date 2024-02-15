from src.db.payment_database import Adicionar_cartao, Adicionar_pix, Adicionar_boleto, atualizar_boleto_pix, obter_lista_de_metodos_pagamento, atualizar_cartao
from src.schemas.payment_schema import Cartao, Pix, Boleto, CartaoUpdate, PixUpdate, BoletoUpdate
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
    
    @staticmethod
    def get_payment_methods(cpf: str): 
        
        resultado = obter_lista_de_metodos_pagamento(cpf)

        if resultado is None: 
            return HTTPPaymentResponse.INEXISTENT_USER()
        else: 
            return resultado
    
    @staticmethod
    def update_cartao(id: int, cartao: CartaoUpdate): 

        sucesso, problemas = atualizar_cartao(id, *cartao.model_dump().values())

        if not sucesso: 

            if "VALIDADE" in problemas: 
                return HTTPPaymentResponse.BAD_REQUEST()
            
            if "ID_NOT_FOUND" in problemas: 
                return HTTPPaymentResponse.INEXISTENT_ID()
            
        return HTTPPaymentResponse.UPDATE_SUCESSFULLY()

    @staticmethod
    def update_pix(id:int, pix: PixUpdate): 

        sucesso = atualizar_boleto_pix(id, *pix.model_dump().values())

        if not sucesso: 
            
            return HTTPPaymentResponse.INEXISTENT_ID()
            
        return HTTPPaymentResponse.UPDATE_SUCESSFULLY()
    
    @staticmethod
    def update_boleto(id:int, boleto: BoletoUpdate): 

        sucesso = atualizar_boleto_pix(id, *boleto.model_dump().values())

        if not sucesso: 
            
            return HTTPPaymentResponse.INEXISTENT_ID()
            
        return HTTPPaymentResponse.UPDATE_SUCESSFULLY()