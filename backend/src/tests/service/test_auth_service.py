import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.user_database import User, UserDatabase
from src.schemas.user_response import HTTPLoginResponses, HTTPVerifyResponses
from random import randrange
from bidict import bidict
from src.service.impl.__init__ import token_service
from src.schemas.user_schemas import DadosLogin, DadosUser
from test_singup_service import sign_up_user
from src.service.impl.auth_service import AuthService
from src.schemas.user_schemas import DadosLogin, DadosUser
from src.db.__init__ import user_database_example as db

def test_login_user():
    # Cadastrar
    cpf1, cpf2, senha = sign_up_user(True)
    dados = DadosLogin(cpf_ou_user_ou_email=cpf1, senha=senha)
    res = AuthService.login_user(dados, db)
    assert res.message == "Login com sucesso"
    assert res.status_code == 200
    assert "token" in res.data
    
    
    db.remove_user_by_cpf(cpf1)
    db.remove_user_by_cpf(cpf2)

def test_login_with_token():
    # Cadastrar
    cpf1, cpf2, senha = sign_up_user(True)
    dados = DadosLogin(cpf_ou_user_ou_email=cpf1, senha=senha)
    res = AuthService.login_user(dados, db)
    
    token = res.data['token']
    res2 = AuthService.login_with_token(token)
    assert res2 == HTTPLoginResponses.LOGIN_SUCCESSFUL(token)
    
    res3 = AuthService.login_with_token(3)
    assert res3 == HTTPLoginResponses.LOGIN_FAILED()
    
    db.remove_user_by_cpf(cpf1)
    db.remove_user_by_cpf(cpf2)

def test_get_user_data():
    cpf1, cpf2, senha = sign_up_user(True)
    dados = DadosLogin(cpf_ou_user_ou_email=cpf1, senha=senha)
    res = AuthService.login_user(dados, db)
    
    token = res.data['token']
    res2 = AuthService.get_user_data(token)
    
    assert res2.data['user'].cpf == cpf1

def test_unlogin_user():
    cpf1, cpf2, senha = sign_up_user(True)
    dados = DadosLogin(cpf_ou_user_ou_email=cpf1, senha=senha)
    res_login = AuthService.login_user(dados, db)
    token = res_login.data['token']
    
    res_get = AuthService.get_user_data(token)
    assert res_get.message == "Usuário retornado"
    
    res = AuthService.unlogin_user_internal(token)
    assert res is not None
    
    res2 = AuthService.unlogin_user_internal(token)
    assert res2 is None
    
    res_get = AuthService.get_user_data(token)
    assert res_get == HTTPVerifyResponses.VERIFY_FAIL()
    
    res3 = AuthService.unlogin_user_internal("13224353")
    assert res3 is None
    