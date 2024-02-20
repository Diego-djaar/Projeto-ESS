from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel

class HTTPSignUpResponses:


    @staticmethod
    def CNPJ_ALREADY_EXIST() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Já existe uma loja registrada com esse CNPJ",
            status_code=401,
        )
        
    @staticmethod
    def NAME_ALREADY_EXIST() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Já existe uma loja registrada com esse Nome",
            status_code=401,
        )
    
    @staticmethod
    def ALREADY_EXIST() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Já existe uma loja registrada com esses dados",
            status_code=401,
        )
    
    @staticmethod
    def BAD_REQUEST() -> HttpResponseModel:  
        return HttpResponseModel(
            message="Request mal feito",
            status_code=400
        )

    @staticmethod
    def SIGNUP_SUCCESSFUL() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Loja cadastrada com sucesso",
            status_code=200,
        )
        
class HTTPLoginResponses:

    @staticmethod
    def STORE_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message = "CNPJ ou Senha incorretos",
            status_code = 401
        )
        
    @staticmethod
    def LOGIN_SUCCESSFUL() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Login com sucesso",
            status_code=200,
        )
    
    @staticmethod
    def LOGIN_FAILED() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Login falhou",
            status_code = 401
        )
        
        

class HTTPUpdateUserResponses:
    @staticmethod
    def REMOVE() -> HttpResponseModel:
        return HttpResponseModel(
            message="Usuário deletado",
            status_code=200
        )
        
    @staticmethod
    def REMOVE_FAIL() -> HttpResponseModel:
        return HttpResponseModel(
            message="Deletar usuário falhou",
            status_code=400
        )
    
    @staticmethod
    def UPDATE_FAIL() -> HttpResponseModel:
        return HttpResponseModel(
            message="Atualizar dados de usuário falhou",
            status_code=400
        )
    
    @staticmethod
    def UPDATE_SUCCESS() -> HttpResponseModel:
        return HttpResponseModel(
            message="Atualização de dados bem sucedida",
            status_code=200
        )
    
    def UNAUTORIZED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Não tem autorização para realizar essa requisição",
            status_code=401
        )