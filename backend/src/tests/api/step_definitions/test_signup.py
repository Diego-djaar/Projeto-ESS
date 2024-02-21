from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.db.__init__ import user_database
from src.db.user_database import User
from pytest_bdd import parsers, given, when, then, scenario
import datetime
import pytest
from src.main import app

TESTCLIENT = TestClient(app)

@pytest.fixture(autouse=True)
def remove_enzo_from_db():
    user_database.remove_user_by_cpf("453.456.426-95")
    enzo_user = user_database.get_user_by_username("Enzo")
    if enzo_user is not None:
        user_database.remove_user_by_cpf(enzo_user.cpf)

"""Scenario: Processar dados cadastrais bem sucedido"""
@scenario(scenario_name="Processar dados cadastrais bem sucedido", feature_name="../features/user_signup.feature")
def test_signup():
    """Process Sign Up data"""

"""Scenario: Processar dados cadastrais mal sucedido"""
@scenario(scenario_name="Processar dados cadastrais mal sucedido", feature_name="../features/user_signup.feature")
def test_signup_fail():
    """Process Sign Up data and return error"""
    
@then(parsers.cfparse('Usuário "{username}" está cadastrado'))
@given(parsers.cfparse('Usuário "{username}" está cadastrado'))
def verify_user(username: str):
    """
        Assert that an user exists in db

    Args:
        user (str): _description_
    """
    assert user_database.get_user_by_username(username) is not None
    
@given(parsers.cfparse('Usuário "{username}" não está cadastrado'))
def verify_user(username: str):
    """
        Assert that an user exists in db

    Args:
        user (str): _description_
    """
    assert user_database.get_user_by_username(username) is None

@when(
    parsers.cfparse('uma requisição "{request_type}" for enviada para "{signup}", com Dados Cadastrais('\
    'nome: "{nome}", sobrenome: "{sobrenome}", user: "{username}", CPF: {cpf}, endereço:  "{endereço}", '\
    'CEP: "{cep}", data de nascimento: "{data_de_nascimento}", email: "{email}", senha: "{senha}")'),
    target_fixture="request_response"
)
def signup_request(
    request_type: str, 
    signup: str, 
    nome: str,
    sobrenome: str,
    username: str, 
    cpf: str,
    endereço: str,
    cep: str,
    data_de_nascimento: str,
    email: str,
    senha: str, 
    client=TESTCLIENT
):
    signup_request = {
        "username": username,
        "nome": nome,
        "sobrenome": sobrenome,
        "cpf": cpf,
        "data_de_nascimento": data_de_nascimento,
        "email": email,
        "senha": senha,
        "endereço": endereço,
        "CEP": cep
    }
    post_ = getattr(client, request_type.lower())
    return post_("/backend/api/auth/user/" + signup, json=signup_request)


@then(parsers.cfparse('o status da resposta deve ser "{status}"'))
def check_response_status(status: str, request_response):
    assert int(status) == request_response.status_code

@then('o JSON da resposta indica que o cadastro foi bem sucedido')
def check_response_json(request_response):
    request_response_json = request_response.json()
    assert request_response_json['message'] == "Usuário cadastrado com sucesso"

@then('o JSON da resposta indica que o cadastro foi mal sucedido')
def check_response_fail_json(request_response):
    request_response_json = request_response.json()
    assert request_response_json['message'] != "Usuário cadastrado com sucesso"
    
@then(parsers.cfparse('o JSON da resposta indica que o campo "{campo}" foi mal preenchido'))
def check_response_field_fail_json(campo: str, request_response):
    request_response_json = request_response.json()
    assert f"Campo {campo} mal formulado" in request_response_json['data']