from src.db.payment_database import Adicionar_cartao, Adicionar_pix, Adicionar_boleto, atualizar_boleto_pix, obter_lista_de_metodos_pagamento, atualizar_cartao, deletar_metodo
from src.schemas.payment_schema import Cartao, Pix, Boleto, CartaoUpdate, PixUpdate, BoletoUpdate
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.payment_response import HTTPPaymentResponse

class PaymentService:

    @staticmethod
    def inserting_card(cartao: Cartao) -> HttpResponseModel:

        sucesso, problemas = Adicionar_cartao(*cartao.model_dump().values())

        if sucesso: 
            return HTTPPaymentResponse.INSERTION_SUCESSFULLY()
        else: 
            return HTTPPaymentResponse.BAD_REQUEST(problemas)
    
    @staticmethod
    def insertion_pix(pix: Pix) -> HttpResponseModel: 

        sucesso, problemas = Adicionar_pix(*pix.model_dump().values())

        if not sucesso:
            return HTTPPaymentResponse.BAD_REQUEST(problemas)

        return HTTPPaymentResponse.INSERTION_SUCESSFULLY()
    
    @staticmethod
    def insertion_ticket(boleto: Boleto) -> HttpResponseModel: 

        sucesso, problemas = Adicionar_pix(*boleto.model_dump().values())

        if not sucesso:
            return HTTPPaymentResponse.BAD_REQUEST(problemas)

        return HTTPPaymentResponse.INSERTION_SUCESSFULLY()
    
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

    @staticmethod
    def delete_method(id: int):

        sucesso = deletar_metodo(id)

        if not sucesso: 

            return HTTPPaymentResponse.INEXISTENT_ID()
        
        return HTTPPaymentResponse.DELETE_SUCESSFULLY()
