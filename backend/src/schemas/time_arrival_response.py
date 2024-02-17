from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPTime_arrivalResponse:

    @staticmethod
    def INSERTION_SUCESSFULLY() -> HttpResponseModel: 
        return HttpResponseModel (
            message="Pré-ordem do produto criada com sucesso!",
            status_code=201
        ) 

    @staticmethod
    def BAD_REQUEST() -> HttpResponseModel:

        return HttpResponseModel (
            message="Informações inválidas", 
            status_code= 400,
            data=["CEP"]
        )

    @staticmethod
    def UPDATE_SUCESSFULLY() -> HttpResponseModel:

        return HttpResponseModel (
            message="Pré-ordem atualizada com sucesso", 
            status_code=200
        ) 

    @staticmethod
    def DELETE_SUCESSFULLY() -> HttpResponseModel:

        return HttpResponseModel (
            message="Pré-ordem deletada com sucesso", 
            status_code=200
        ) 
