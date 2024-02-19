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


@scenario(scenario_name= "Obter carrinho por CPF", feature_name="..//features/carrinho.feature")
def test_get_cart_by_CPF():
    pass

@scenario(scenario_name="Adicionar um produto válido ao carrinho", feature_name="..//features/carrinho.feature")
def test_add_valid_product_to_cart():
    pass

@given(parsers.cfparse('o Carrinho_service retorna um carrinho com cpf "{CPF}"'))
def mock_cart_service_response(CPF: str):
    #Carrinho_service.get_cart = lambda CPF: HttpResponseModel(
    #    message=HTTPResponses.ITEM_FOUND().message,
    #    status_code=HTTPResponses.ITEM_FOUND().status_code,
    #    data={"Itens:": {}, "Total": "0.00", "Endereço": "Endereço não registrado"}
    #)
    pass

@given(parsers.cfparse('um produto com ID "{id}" está disponível'))
def produto_disponivel(id: str):
    # Adicionar lógica para verificar se o produto está disponível na base de dados
    pass

@given(parsers.cfparse('o carrinho do cliente com CPF "{CPF}" está vazio'), target_fixture="context")
def carrinho_vazio(context, CPF: str):
    # Inicialização do carrinho
    context['CPF'] = CPF
    response = TESTCLIENT.get(url="/carrinho/view/123.456.789-10")
    assert response.status_code == 200
    return context

@when(parsers.cfparse('o cliente adiciona o produto com ID "{id}" ao carrinho'), target_fixture="context")
def adiciona_produto_ao_carrinho(context, id: str):
    response = TESTCLIENT.post("/carrinho/adicionar", 
                               json={
                                        "id": "12345678",
                                        "nome": "Camisa",
                                        "description": "string",
                                        "price": "29.99",
                                        "quantidade": 1,
                                        "img": "string.jpg"
                                    }, 
                                    params={"CPF": context["CPF"]})
    context["response"] = response
    return context

@then(parsers.cfparse('o item deve estar no carrinho'), target_fixture="context")
def verificar_item_no_carrinho(context):
    response = Carrinho_service.get_cart(context["CPF"])
    cart_dict = response.data # Da forma {"Itens": dict[Item], "Total": "20.99", "Endereço": "Endereço não registrado"}
    #assert context["CPF"] in cart_dict["Itens"].keys()
    return context

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
    expected_data = {"Itens:": [], "Total": "0.00", "Endereço": "Endereço não registrado"}
    assert context["response"].json()["data"] == expected_data
    return context