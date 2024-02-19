from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.db.__init__ import user_database
from src.db.user_database import User
from pytest_bdd import parsers, given, when, then, scenario
import datetime
import pytest
from src.main import app

TESTCLIENT = TestClient(app)

# Set presumed initial conditions for testing
@pytest.fixture(scope="session", autouse=True)
def database_setup():
    user_database.remove_user_by_cpf("453.456.426-95")
    enzo_user = user_database.get_user_by_username("Enzo")
    if enzo_user is not None:
        user_database.remove_user_by_cpf(enzo_user.cpf)
    user_gabriel = User.new(
        "Gabriel",
        "Gabriel Souza",
        "de Lima",
        "453.456.426-95",
        datetime.date.fromisocalendar(1984, 42, 7),
        "gabriel@gogle.com",
        "senha1234"
    )[0]
    user_database.add_user(user_gabriel)
    
    yield
    
    user_database.remove_user_by_cpf("453.456.426-95")


"""Scenario: processar dados de login"""
@scenario(scenario_name="processar dados de login", feature_name="../features/login.feature")
def test_login():
    """Process Login data"""

"""Scenario: processar dados de login com usuário inexistente"""
@scenario(scenario_name="processar dados de login com usuário inexistente", feature_name="../features/login.feature")
def test_login_fail():
    """Process Login data and return error"""

"""Scenario: processar dados de login com senha incorreta"""
@scenario(scenario_name="processar dados de login com senha incorreta", feature_name="../features/login.feature")
def test_login_fail_psw():
    """Process Login data and return error"""
    
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
    
@given(parsers.cfparse('Usuário "{username}" possui senha "{senha}"'))
def verify_psw(username: str, senha: str):
    """
        Assert user password

    Args:
        username (str): _description_
        senha (str): _description_
    """
    user: User = user_database.get_user_by_username(username)
    assert user.check_password(senha)
    
@when(
    parsers.cfparse('uma requisição "{request_type}" for enviada para "{login}", com Dados Login(usuário: "{username}", senha: "{senha}")'),
    target_fixture="request_response"
)
def login_request(request_type: str, login: str, username: str, senha: str, client=TESTCLIENT):
    """
        Faz uma requisição de login

    Args:
        request_type (str): _description_
        username (str): _description_
        senha (str): _description_
        client (_type_, optional): _description_. Defaults to TestClient.
    """
    login_request = {
        "cpf_ou_user_ou_email": username,
        "senha": senha
    }
    post_ = getattr(client, request_type.lower())
    return post_("/backend/api/auth/user/" + login, json=login_request)

@then(parsers.cfparse('o status da resposta deve ser "{status}"'))
def check_response_status(status: str, request_response):
    # print('\n\nresponse = ', request_response, '\n\n')
    assert int(status) == request_response.status_code

@then(
    parsers.cfparse('o campo "{campo1}" possui o campo "{token}" com valor "$token_valor"'),
    target_fixture="token_value"
)
def check_field_token(campo1: str, token: str, request_response):
    request_response_json = request_response.json()
    field = request_response_json[campo1][token]
    return field

@when(
    parsers.cfparse('uma requisição "{request_type}" for enviada para "{verify}", com "$token_valor"'),
    target_fixture="request_response"
)
def verify_request(request_type: str, verify: str, token_value, client = TESTCLIENT):
    verify_request = {
        "token" : token_value
    }
    post_ = getattr(client, request_type.lower())
    return post_("/backend/api/auth/user/" + verify, json=verify_request)

@then(
    parsers.cfparse('o campo "{campo1}" possui o campo "{campo2}"'),
    target_fixture="campo_value"
)
def check_field(campo1: str, campo2: str, request_response):
    request_response_json = request_response.json()
    field = request_response_json[campo1][campo2]
    return field

@then(
    parsers.cfparse('os elementos de "user" correspondem aos dados do usuário "{username}"')
)
def check_user_data(username: str, campo_value):
    user: User = user_database.get_user_by_username(username)
    assert user.username == campo_value['username']
    assert user.nome == campo_value['nome']
    assert user.sobrenome == campo_value['sobrenome']
    assert user.cpf == campo_value['cpf']
    


@then(
    parsers.cfparse('o campo "{campo1}" tem o valor "{value}"')
)
def check_field_value(campo1: str, value: str, request_response):
    request_response_json = request_response.json()
    field = request_response_json[campo1]
    assert field == value


