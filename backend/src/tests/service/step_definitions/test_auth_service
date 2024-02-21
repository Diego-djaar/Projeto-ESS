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
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.db.__init__ import user_database
from src.db.user_database import User
from pytest_bdd import parsers, given, when, then, scenario
import pytest

@pytest.fixture(scope="session", autouse=True)
def database_setup():
    user = User.new(
        "Cleiton",
        "Cleiton Moura",
        "da Silva",
        "444.324.424-09",
        datetime.date.fromisocalendar(1,1,1),
        "Cleiton@momo",
        "12345Abcx" 
    )
    user_database.add_user(user)
    
    yield
    
    user_database.remove_user_by_cpf("444.324.424-09")

"""Scenario: login user"""
@scenario(scenario_name=" login user", feature_name="../features/auth_service.feature")
def test_login():
    """User login"""
    
"""Scenario: login user fail"""
@scenario(scenario_name=" login user fail", feature_name="../features/auth_service.feature")
def test_login_fail():
    """User login fail"""
    
"""Scenario: login user fail 2"""
@scenario(scenario_name=" login user fail 2", feature_name="../features/auth_service.feature")
def test_login_fail2():
    """User login fail"""
    
@given(parsers.cfparse('Usuário com Cpf "{cpf}" não está cadastrado'))
def check_cpf(cpf: str):
    assert user_database.get_user_by_cpf(cpf) is None
    
@given(parsers.cfparse('Usuário com Cpf "{cpf}" está cadastrado'),
target_fixture="user_")
def check_cpf(cpf: str):
    user = user_database.get_user_by_cpf(cpf)
    assert user is not None
    return user

@given(parsers.cfparse('o usuário possui a senha "{senha}"'))
def check_psw(senha: str, user_: User):
    assert user_.check_password(senha)
    
@when(parsers.cfparse('o método Login User é chamado com DadosLogin(cpf_ou_user_ou_email="{cpf}", senha="{senha}")'),
target_fixture="response")
def login(cpf: str, senha: str):
    dados = DadosLogin(cpf_ou_user_ou_email=cpf, senha=senha)
    res = AuthService.login_user(dados)
    return res

@then('o método deve retornar que o login foi bem sucedido')
def check_success(response):
    assert response == HTTPLoginResponses.LOGIN_SUCCESSFUL()

@then('o método deve retornar que o login foi mal sucedido')
def check_fail(response):
    assert response == HTTPLoginResponses.LOGIN_FAILED()

@then(parsers.cfparse('o campo "{campo}" da resposta deve conter o valor "{value}"'))
def check_value(campo: str, value: str, response):
    assert getattr(response, campo) == value
    
@then(parsers.cfparse('o campo "{campo1}" da resposta deve conter o campo "{campo2}"'))
def check_field(campo1: str, campo2: str, response):
    assert getattr(response, campo1)[campo2]
    

