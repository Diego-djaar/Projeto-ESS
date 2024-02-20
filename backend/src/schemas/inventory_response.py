from typing import Optional
from pydantic import BaseModel
from src.schemas.response import HttpResponseModel


class HTTPItemResponses:

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
            status_code = 400
        )
    
    @staticmethod
    def NO_ITEM_IN_DATABASE() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Nenhum item encontrado na base de dados",
            status_code=404,
        )
    
    @staticmethod
    def BAD_REQUEST(reason_list: list[str]) -> HttpResponseModel:
        # Cria uma mensagem detalhada com base na lista de razões
        detailed_message = "Solicitação mal feita. Motivos: " + "; ".join(reason_list)
    
        return HttpResponseModel(
            message=detailed_message,
            status_code=400
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

    @staticmethod
    def UNAUTHORIZED() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Item não pertence à loja",
            status_code=403,
        )