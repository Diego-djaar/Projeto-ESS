from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPPaymentResponse:

    @staticmethod
    def INSERTION_SUCESSFULLY(id: str) -> HttpResponseModel: 
        return HttpResponseModel (
            message="metodo de pagamento cadastrado com sucesso",
            status_code=201, 
            data = {
                "ID": id 
            }
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
            message=f" informações inválidas", 
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
    
    @staticmethod
    def DELETE_SUCESSFULLY() -> HttpResponseModel:

        return HttpResponseModel (
            message="Deleção realizada com sucesso", 
            status_code=200
        ) 
    
    @staticmethod
    def PIX_ALREADY_EXIST() -> HttpResponseModel:

        return HttpResponseModel (
            message="Já existe um pix cadastrado no sistema", 
            status_code=400
        )
        
    @staticmethod
    def BOLETO_ALREADY_EXIST() -> HttpResponseModel:

        return HttpResponseModel (
            message="Já existe um boleto cadastrado no sistema", 
            status_code=400
        )
    