from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPSignUpResponses:

    """
    Contém respostas http referentes ao cadastro de usuário
    """

    @staticmethod
    def USER_ALREADY_EXIST() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Já existe uma conta com esse User",
            status_code=401,
        )
        
    @staticmethod
    def CPF_ALREADY_EXIST() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Já existe uma conta com esse CPF",
            status_code=401,
        )
    
    def BAD_REQUEST(reason_: str) -> HttpResponseModel:
        return HttpResponseModel(
            message="Request mal feito",
            data=[f"Campo {reason_} mal formulado"],
            status_code=400
        )

    @staticmethod
    def SIGNUP_SUCCESSFUL() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Usuário cadastrado com sucesso",
            status_code=200,
        )