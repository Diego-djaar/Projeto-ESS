import datetime
from pydantic import BaseModel
from schemas.response import HTTPResponses, HttpResponseModel
from db.__init__ import user_database as db
from db.user_database import User, UserDatabase
from schemas.user_response import HTTPLoginResponses, HTTPVerifyResponses
from random import randrange
from bidict import bidict
from service.impl.__init__ import token_service
from schemas.user_schemas import DadosLogin, DadosUser


class AuthService():
    @staticmethod
    def login_user(dados_login: DadosLogin, dbase = db) -> HttpResponseModel:
        """Tenta realizar o login do usuário

        Args:
            dados_login (DadosCadastrais): _description_

        Returns:
            HttpResponseModel: _description_
        """
        user_credencial = dados_login.cpf_ou_user_ou_email
        user_senha = dados_login.senha
        
        user = dbase.get_user_by_cpf(user_credencial)
        
        if user == None:
            user = dbase.get_user_by_email(user_credencial)
        
        if user == None:
            user= dbase.get_user_by_username(user_credencial)
        
        if user == None or not user.check_password(user_senha):
            return HTTPLoginResponses.USER_NOT_FOUND()
        
        token = token_service.add_user(user)
        
        return HTTPLoginResponses.LOGIN_SUCCESSFUL(token)
    
    @staticmethod
    def login_with_token(token: str) -> HttpResponseModel:
        token = int(token)
        if token_service.user_active(token):
            return HTTPLoginResponses.LOGIN_SUCCESSFUL(token)
        else:
            return HTTPLoginResponses.LOGIN_FAILED()
        
    
    @staticmethod
    def get_user_data(token: str) -> HttpResponseModel:
        token = int(token)
        user: User = token_service.get_user_of_token(token)
        if user == None:
            return HTTPVerifyResponses.VERIFY_FAIL()
        else:
            data = DadosUser.from_user(user)
            return HTTPVerifyResponses.VERIFY(data)
        
    @staticmethod
    def unlogin_user_internal(token: str) -> DadosUser:
        token = int(token)
        user: User = token_service.get_user_of_token(token)
        if user is None:
            return None
        token_service.rm_user(token)
        return DadosUser.from_user(user)
    
    # @staticmethod
    # def unlogin_user(token: str) -> HttpResponseModel:
    #     dados_user = AuthService.unlogin_user_internal(token)
    #     if dados_user is None:
    #         return HTTPLoginResponses.UNLOGIN_FAILED()
    #     token_service.rm_user(token)
    #     return HTTPLoginResponses.UNLOGIN_SUCCESSFUL()
