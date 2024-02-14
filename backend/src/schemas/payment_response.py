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