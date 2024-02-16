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
            data.append(f"Já existe um item com esse ID")
        
        return HttpResponseModel(
            message = "Já existe um item com esse ID",
            data = data,
            status_code = 401,
        )