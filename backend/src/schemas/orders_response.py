from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPOrdersResponse:

    @staticmethod
    def CANCEL_SUCCESSFULLY() -> HttpResponseModel: 
        return HttpResponseModel (
            message="Pedido cancelado com sucesso",
            status_code=200,
        ) 

    @staticmethod
    def BAD_REQUEST(errors) -> HttpResponseModel:

        if ('canceled' in errors):
            return HttpResponseModel (
                message="O pedido já foi cancelado!", 
                status_code= 400, 
            )
        elif ('delivered' in errors):
            return HttpResponseModel (
                message="O pedido já foi entregue!", 
                status_code= 400,
            )
        elif ('No cancel reason' in errors):
            return HttpResponseModel (
                message="O usuário não colocou a razão de cancelamento!", 
                status_code= 400
            )
        elif ('CPF not found' in errors):
            return HttpResponseModel (
                    message="Não consta pedidos no CPF", 
                    status_code= 400
                )
        elif ("ID not found" in errors):
            return HttpResponseModel(
                message="O usuário não tem pedido com este ID",
                status_code=400
            )
        else:
            return HttpResponseModel(
                message="Bad request",
                status_code= 400
            )
    
    @staticmethod
    def GET_SUCCESSFULLY(orders_canceled) -> HttpResponseModel:

        return HttpResponseModel (
            message="Pedido obtidos com sucesso",
            status_code=200,
            data=orders_canceled
        ) 
    
    @staticmethod
    def NO_CANCEL_ORDERS() -> HttpResponseModel:

        return HttpResponseModel (
            message="O usuário não tem pedidos cancelados",
            status_code=400
        ) 
