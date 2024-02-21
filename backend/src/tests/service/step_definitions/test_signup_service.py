from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.db.__init__ import user_database
from src.db.user_database import User
from pytest_bdd import parsers, given, when, then, scenario
import datetime
import pytest
from src.db.user_database import User, UserDatabase
from bcrypt import hashpw, checkpw, gensalt
import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.__init__ import user_database_example as db
from src.db.user_database import User, UserDatabase
from src.schemas.user_response import HTTPSignUpResponses
import src.service.impl.signup_service as signup
import src.db.user_database as dbase

"""Scenario: Sign Up User"""
@scenario(scenario_name="Sign Up User", feature_name="../features/signup_service.feature")
def test_signup():
    """User signup"""
    
"""Scenario: Sign Up já existente"""
@scenario(scenario_name="Sign Up já existente", feature_name="../features/signup_service.feature")
def test_signup_existing_user():
    """User signup fail"""
    
"""Scenario: Sign Up cpf mal formulado"""
@scenario(scenario_name="Sign Up cpf mal formulado", feature_name="../features/signup_service.feature")
def test_signup_bad_cpf():
    """User signup bad request"""
    
@given(parsers.cfparse('Usuário com Cpf "{cpf}" não está cadastrado'))
def check_cpf(cpf: str):
    assert user_database.get_user_by_cpf(cpf) is None
    
@given(parsers.cfparse('Usuário com Cpf "{cpf}" está cadastrado'))
def check_cpf(cpf: str):
    assert user_database.get_user_by_cpf(cpf) is not None
    
@when(parsers.cfparse('o método de Sign Up é chamada com Dados Cadastrais username= "{username}", nome = "{nome}", sobrenome = "{sobrenome}", cpf = "{cpf}", data_de_nascimento="{data_de_nascimento}", email="{email}", senha="{senha}", endereço = "{endereço}", CEP = "{cep}"'),
target_fixture="signup_response"      
)
def signup_call(username: str, nome: str, sobrenome: str, cpf: str, data_de_nascimento: str, email: str, senha: str, endereço: str, cep: str):
    if endereço == "None":
        endereço = None
    if cep == "None":
        cep = None
    dados_cadastrais = signup.DadosCadastrais(
        username= username,
        nome = nome,
        sobrenome = sobrenome,
        cpf = cpf,
        data_de_nascimento=eval(data_de_nascimento),
        email=email,
        senha=senha,
        endereço = endereço,
        CEP = cep
    )
    return signup.SingUpService.signup_user(dados_cadastrais, user_database)

@then('o método deve retornar que o Sign Up foi bem sucedido')
def signup_success(signup_response):
    res: HttpResponseModel = signup_response
    assert res == HTTPSignUpResponses.SIGNUP_SUCCESSFUL()
    
@then('o método deve retornar que o Sign Up foi mal sucedido')
def signup_failure(signup_response):
    res: HttpResponseModel = signup_response
    assert res != HTTPSignUpResponses.SIGNUP_SUCCESSFUL()
    
@then(parsers.cfparse('o campo "{campo}" da resposta deve conter "{aviso}"'))
def check_data_response(campo: str, aviso: str, signup_response):
    res: HttpResponseModel = signup_response
    data = getattr(signup_response, campo)
    assert aviso in data