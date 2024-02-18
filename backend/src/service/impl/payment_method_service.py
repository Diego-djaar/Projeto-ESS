from src.db.payment_database import *
from src.schemas.payment_schema import Cartao, Pix, Boleto, CartaoUpdate, PixUpdate, BoletoUpdate
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.payment_response import HTTPPaymentResponse

class PaymentService:

    @staticmethod
    def inserting_card(cartao: Cartao) -> HttpResponseModel:

        sucess, problems = insert_card(*cartao.model_dump().values())

        if sucess: 
            return HTTPPaymentResponse.INSERTION_SUCESSFULLY(problems)
        else: 
            return HTTPPaymentResponse.BAD_REQUEST(problems)
    
    @staticmethod
    def insertion_pix(pix: Pix) -> HttpResponseModel: 

        result, id = insert_pix(*pix.model_dump().values())

        if result == "CPF":
            return HTTPPaymentResponse.BAD_REQUEST(["CPF"])
        elif result == "ALREADY_EXIST":
            return HTTPPaymentResponse.PIX_ALREADY_EXIST()

        return HTTPPaymentResponse.INSERTION_SUCESSFULLY(id)
    
    @staticmethod
    def insertion_ticket(boleto: Boleto) -> HttpResponseModel: 

        result, id = insert_ticket(*boleto.model_dump().values())

        if result == "CPF":
            return HTTPPaymentResponse.BAD_REQUEST(["CPF"])
        elif result == "ALREADY_EXIST":
            return HTTPPaymentResponse.BOLETO_ALREADY_EXIST()

        return HTTPPaymentResponse.INSERTION_SUCESSFULLY(id)
    
    # @staticmethod
    # def get_payment_methods(cpf: str): 
        
    #     resultado = obter_lista_de_metodos_pagamento(cpf)

    #     if resultado is None: 
    #         return HTTPPaymentResponse.INEXISTENT_USER()
    #     else: 
    #         return resultado
    
    @staticmethod
    def update_card(id: int, cartao: CartaoUpdate): 

        sucess, problems = update_card(id, *cartao.model_dump().values())

        if not sucess: 

            if "VALIDADE" in problems: 
                return HTTPPaymentResponse.BAD_REQUEST()
            
            if "ID_NOT_FOUND" in problems: 
                return HTTPPaymentResponse.INEXISTENT_ID()
            
        return HTTPPaymentResponse.UPDATE_SUCESSFULLY()

    @staticmethod
    def update_pix(id:int, pix: PixUpdate): 

        sucess = update_pix_or_ticket(id, *pix.model_dump().values())

        if not sucess: 
            
            return HTTPPaymentResponse.INEXISTENT_ID()
            
        return HTTPPaymentResponse.UPDATE_SUCESSFULLY()
    
    @staticmethod
    def update_ticket(id:int, boleto: BoletoUpdate): 

        sucess = update_pix_or_ticket(id, *boleto.model_dump().values())

        if not sucess: 
            
            return HTTPPaymentResponse.INEXISTENT_ID()
            
        return HTTPPaymentResponse.UPDATE_SUCESSFULLY()

    @staticmethod
    def delete_method(id: int):

        sucess = delete_method(id)

        if not sucess: 

            return HTTPPaymentResponse.INEXISTENT_ID()
        
        return HTTPPaymentResponse.DELETE_SUCESSFULLY()