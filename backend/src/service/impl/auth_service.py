import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.__init__ import user_database as db
from src.db.user_database import User, UserDatabase
from src.schemas.user_response import HTTPLoginResponses, HTTPVerifyResponses
from random import randrange
from bidict import bidict
from src.service.impl.__init__ import token_service
from src.schemas.user_schemas import DadosLogin, DadosUser


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
            data = DadosUser(
                username=user.username,
                nome=user.nome,
                sobrenome=user.sobrenome,
                cpf=user.cpf,
                data_de_nascimento=user.data_de_nascimento,
                email=user.email,
                CEP=user.CEP
            )
            return HTTPVerifyResponses.VERIFY(data)
