from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPCarrinhoResponses():
    """ Respostas HTTP padronizadas para o carrinho """
    @staticmethod
    def CART_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Carrinho não encontrado",
            status_code=404,
        )
    
    @staticmethod
    def REMOVE_ITEM_SUCCESSFULLY() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Item removido com sucesso",
            status_code=200,
        )
    
    @staticmethod
    def DECREASE_ITEM_QUANTITY(reason: str) -> HttpResponseModel:
        return HttpResponseModel(
            message= reason,
            status_code=200
        )
    
    @staticmethod
    def MODIFY_ITEM_QUANTITY() -> HttpResponseModel:
        return HttpResponseModel(
            message= "Quantidade do item alterada com sucesso",
            status_code=200
        )
    
    @staticmethod
    def CLEAR_CART(success: bool) -> HttpResponseModel:
        if success:
            return HttpResponseModel(
                message= "Conteúdo do carrinho limpo com sucesso",
                status_code=200
            )
        return HTTPCarrinhoResponses.CART_NOT_FOUND()
    
    @staticmethod
    def CLEAR_ALL_CARTS() -> HttpResponseModel:
        return HttpResponseModel(
            message= "Conteúdo da database de carrinhos limpo",
            status_code=200
        )
    
    @staticmethod
    def MODIFY_ADRESS_SUCCESFULLY() -> HttpResponseModel:
        return HttpResponseModel(
            message="Endereço alterado com sucesso",
            status_code=200
        )