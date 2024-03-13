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
    
"""Scenario: Logar e usar carrinho"""
@scenario(scenario_name="Logar e usar carrinho", feature_name="../features/integrate_login_carrinho.feature")
def test_login_cart():
    """Do Login, then access cart"""

@when(parsers.cfparse('uma requisição GET for enviada para "/backend/api/carrinho/view/123.456.789-10"'), target_fixture="context")
def send_get_cart_request(context, cpf = 0, client = TESTCLIENT):
    print("send_get_cart_request")
    print(context)
    response = client.get(url="/backend/api/carrinho/view/" + cpf)
    print(context)
    context["response"] = response
    return context

@when(parsers.cfparse('o cliente adiciona o produto com ID "{id}" ao carrinho'), target_fixture="context")
def adiciona_produto_ao_carrinho(context, id: str, quantidade: int = 1, preço: str = "29.99"):
    response = TESTCLIENT.post("/backend/api/carrinho/adicionar", 
                               json={
                                        "id": str(id),
                                        "nome": "Camisa",
                                        "description": "string",
                                        "price": preço,
                                        "quantidade": quantidade,
                                        "img": "string.jpg"
                                    }, 
                                    params={"CPF": context["CPF"]})
    context["response"] = response
    context["id"] = id 
    return context  

@given(parsers.cfparse('um produto com ID "{id}" está no carrinho de "{user}"'), target_fixture="context")
def adicionar_item_ao_carrinho(context, id: str, user: str):
    context["id"] = id
    context["CPF"] = user_database.get_user_by_username(user).cpf
    cpf = context["CPF"]
    send_get_cart_request(context, cpf)
    adiciona_produto_ao_carrinho(context, id)
    return context

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
    parsers.cfparse('o campo "{campo1}" possui o campo "{token}" com valor $token_valor'),
    target_fixture="token_value"
)
def check_field_token(campo1: str, token: str, request_response):
    request_response_json = request_response.json()
    field = request_response_json[campo1][token]
    return field

@when(
    parsers.cfparse('uma requisição "{request_type}" for enviada para "{verify}", com $token_valor'),
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

@when(parsers.cfparse('o cliente tenta remover o produto com ID "{id}" do carrinho de "{user}"'), target_fixture="context")
def remover_item_do_carrinho(context, id: str, user: str):
    response = TESTCLIENT.delete("/backend/api/carrinho/remover", params={"CPF": user_database.get_user_by_username(user).cpf, "item_id": id})
    context["response"] = response
    return context

def check_response_json(context):
    expected_data = {"Itens": [], "Total": "0.00", "Endereço": "Endereço não registrado"}
    assert context["response"].json()["data"] == expected_data
    return context

@then(parsers.cfparse('o carrinho de "{user}" está vazio'), target_fixture="context")
def empty_cart(context, user):
    send_get_cart_request(context, user_database.get_user_by_username(user).cpf)
    check_response_json(context)
    return context
