from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPTimeArrivalResponse:

    @staticmethod
    def GET_SUCCESSFULLY(data_param) -> HttpResponseModel: 
        return HttpResponseModel (
            message="Tempo estimado do produto calculado com sucesso!",
            status_code=200, 
            data= data_param
        ) 

    @staticmethod
    def BAD_REQUEST(errors) -> HttpResponseModel:

        return HttpResponseModel (
            message="CEP do usuário inválido!", 
            status_code= 400,
            data=["User CEP"]
        )