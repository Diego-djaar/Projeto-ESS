from typing import Optional
from pydantic import BaseModel
from .response import HttpResponseModel
from src.schemas.user_schemas import DadosLogin, DadosUser

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
    
    @staticmethod
    def ALREADY_EXIST(reason_: list[str]) -> HttpResponseModel:
        data = []
        for reas in reason_:
            data.append(f"Já existe uma conta com esse {reas}")
        return HttpResponseModel(
            message = "Já existe uma conta com esses dados",
            data = data,
            status_code=401,
        )
    
    @staticmethod
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
        
class HTTPLoginResponses:
    """
    Contém respostas http referentes ao login de usuário
    """
    
    @staticmethod
    def USER_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message = "CPF ou Senha incorretos",
            status_code = 401
        )
        
    @staticmethod
    def LOGIN_SUCCESSFUL(token: int) -> HttpResponseModel:
        return HttpResponseModel(
            message = "Login com sucesso",
            data = {
                "token": str(token)
            },
            status_code=200,
        )
    
    @staticmethod
    def LOGIN_FAILED() -> HttpResponseModel:
        return HttpResponseModel(
            message = "Login falhou",
            status_code = 401
        )
        
    # @staticmethod
    # def UNLOGIN_SUCCESSFUL() -> HttpResponseModel:
    #     return HttpResponseModel (
    #         message= "Deslogado com sucesso",
    #         status_code=200
    #     )
        
    # @staticmethod
    # def UNLOGIN_FAILED() -> HttpResponseModel:
    #     return HttpResponseModel (
    #         message= "Algo falhou ao tentar deslogar",
    #         status_code=400
    #     )
        
class HTTPVerifyResponses:
    """
    Contém respostas http referentes a verificação de usuário
    """
    def VERIFY(dados_user: DadosUser) -> HttpResponseModel:
        return HttpResponseModel(
            message="Usuário retornado",
            data={
                "user": dados_user
            },
            
                status_code = 200
        )
        
    def VERIFY_FAIL() -> HttpResponseModel:
        return HttpResponseModel(
            message="Verificação falhou",
            status_code=401
        )

class HTTPUpdateUserResponses:
    @staticmethod
    def REMOVE(dados_user: DadosUser) -> HttpResponseModel:
        return HttpResponseModel(
            message="Usuário deletado",
            data={
                "user": dados_user
            },
            status_code=200
        )
        
    @staticmethod
    def REMOVE_FAIL() -> HttpResponseModel:
        return HttpResponseModel(
            message="Deletar usuário falhou",
            status_code=400
        )
    
    @staticmethod
    def UPDATE_FAIL(reason) -> HttpResponseModel:
        return HttpResponseModel(
            message="Atualizar dados de usuário falhou",
            data=reason,
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