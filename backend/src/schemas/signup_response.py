from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPSignUpResponses:

    """
    Contém respostas http referentes ao cadastro de usuário
    """

    @staticmethod
    def USER_ALREADY_EXIST(reason_: list[str]) -> HttpResponseModel:
        data = []
        for reas in reason_:
            data.append(f"Já existe uma conta com esse {reas}")
        return HttpResponseModel(
            message = "Já existe uma conta com esse User",
            data = data,
            status_code=401,
        )
        
    @staticmethod
    def CPF_ALREADY_EXIST(reason_: list[str]) -> HttpResponseModel:
        data = []
        for reas in reason_:
            data.append(f"Já existe uma conta com esse {reas}")
        return HttpResponseModel(
            message = "Já existe uma conta com esse CPF",
            data = data,
            status_code=401,
        )
    
    def BAD_REQUEST(reason_: list[str]) -> HttpResponseModel:
        data = []
        for reas in reason_:
            data.append(f"Campo {reas} mal formulado")
            
        return HttpResponseModel(
            message="Request mal feito",
            data=data,
            status_code=400
        )

    @staticmethod
    def SIGNUP_SUCCESSFUL() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Usuário cadastrado com sucesso",
            status_code=200,
        )