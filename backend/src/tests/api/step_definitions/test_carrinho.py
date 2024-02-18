from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.carrinho_service import Carrinho_service
from src.schemas.response import HttpResponseModel, HTTPResponses
from src.schemas.carrinho_response import HTTPCarrinhoResponses
from fastapi.testclient import TestClient
from src.main import app
import pytest
from src.db.__init__ import cart_database
from src.db.itens_database import Item

TESTCLIENT = TestClient(app)

import pytest

@pytest.fixture(autouse=True)
def clean_database():
    # Código para limpar a base de dados antes de cada teste
    cart_database.clear_cart_database()

    yield

    # Código para limpar a base de dados depois de cada teste (se necessário)
    cart_database.clear_cart_database()


@scenario(scenario_name= "Obter carrinho por CPF", feature_name="..//features/carrinho.feature")
def test_get_cart_by_CPF():
    pass

@given(parsers.cfparse('o Carrinho_service retorna um carrinho com cpf "{CPF}"'))
def mock_cart_service_response(CPF: str):
    Carrinho_service.get_cart = lambda CPF: HttpResponseModel(
        message=HTTPResponses.ITEM_FOUND().message,
        status_code=HTTPResponses.ITEM_FOUND().status_code,
        data={"Itens:": {}, "Total": "0.00", "Endereço": "Endereço não registrado"}
    )


@when(parsers.cfparse('uma requisição GET for enviada para "/carrinho/view/123.456.789-10"'), target_fixture="context")
def send_get_cart_request(context, client = TESTCLIENT):
    response = client.get(url="/carrinho/view/123.456.789-10")
    context["response"] = response
    return context

@then(
    parsers.cfparse('o status da resposta deve ser "200"'), target_fixture="context"
)
def check_response_status_code(context):
    assert context["response"].status_code == 200
    return context

@then(
    parsers.cfparse('o resultado do JSON deve ser "{expected_data}"'),
    target_fixture="context"
)
def check_response_json(context):
    expected_data = {"Itens:": {}, "Total": "0.00", "Endereço": "Endereço não registrado"}
    assert context["response"].json()["data"] == expected_data
    return context