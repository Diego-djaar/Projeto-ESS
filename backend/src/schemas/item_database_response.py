from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPDatabaseResponses:

    """
    Contém respostas http referentes a acessos na base de dados de itens
    """

    @staticmethod
    def ITEM_ALREADY_EXISTS(reason_list: list[str]) -> HttpResponseModel:
        data = []
        for reason in reason_list:
            data.append(reason)
        
        return HttpResponseModel(
            message = "Já existe um item com esse ID",
            data = data,
            status_code = 401
        )
    
    @staticmethod
    def BAD_REQUEST(reason_list: list[str]) -> HttpResponseModel:
        data = []
        for reason in reason_list:
            data.append(reason)
        
        return HttpResponseModel(
            message= "Solicitação mal feita.",
            data= data,
            status_code= 400
        )
    
    @staticmethod
    def ADD_ITEM_SUCCESSFULLY() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Item cadastrado com sucesso",
            status_code=200,
        )
    
    @staticmethod
    def REMOVE_ITEM_SUCCESSFULLY() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Item removido com sucesso",
            status_code=200,
        )
    
    @staticmethod
    def MODIFY_ITEM_SUCCESSFULLY() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Item modificado com sucesso",
            status_code=200,
        )