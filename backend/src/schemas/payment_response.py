from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPPaymentResponse:

    @staticmethod
    def INSERTION_SUCESSFULLY() -> HttpResponseModel: 
        return HttpResponseModel (
            message="Payment method has been inserted sucessfully",
            status_code=201
        )
    
    # @staticmethod
    # def INVALID_CPF() -> HttpResponseModel:
    #     return HttpResponseModel (
    #         message="Invalid CPF",
    #         status_code=400
    #     )
    
    # @staticmethod
    # def EXPIRED_DATA() -> HttpResponseModel:
    #     return HttpResponseModel (
    #         message="The card is expired",
    #         status_code=400
    #     )
    
    # @staticmethod
    # def INVALID_NUMBER() -> HttpResponseModel:
    #     return HttpResponseModel (
    #         message="The card number is invalid", 
    #         status_code=400 
    #     )
    
    @staticmethod
    def BAD_REQUEST(problemas) -> HttpResponseModel:

        return HttpResponseModel (
            message="Os campos a seguir estão preenchidos incorretamente", 
            status_code=400, 
            data= problemas
        )
    
    @staticmethod
    def PIX_INSERTED_SUCESSFULLY() -> HttpResponseModel:

        return HttpResponseModel (
            message="pix inserido com sucesso", 
            status_code=201 
        ) 
    
    @staticmethod
    def BOLETO_INSERTED_SUCESSFULLY() -> HttpResponseModel:

        return HttpResponseModel (
            message="boleto inserido com sucesso", 
            status_code=201 
        ) 
    
    @staticmethod
    def INEXISTENT_USER() -> HttpResponseModel:

        return HttpResponseModel (
            message="O usuário não está registrado na base de dados", 
            status_code=400  
        ) 
    
    @staticmethod
    def INEXISTENT_ID() -> HttpResponseModel:

        return HttpResponseModel (
            message="ID não encontrado na base de dados", 
            status_code=400  
        ) 
    
    @staticmethod
    def UPDATE_SUCESSFULLY() -> HttpResponseModel:

        return HttpResponseModel (
            message="Dados atualizados com sucesso", 
            status_code=200
        ) 
    