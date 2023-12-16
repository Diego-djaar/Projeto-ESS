from typing import Optional
from pydantic import BaseModel

class HttpResponseModel(BaseModel):
    message: str
    status_code: int
    data: Optional[dict] | Optional[list] = None

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

    @staticmethod
    def SIGNUP_SUCCESSFUL() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Usuário cadastrado com sucesso",
            status_code=200,
        )