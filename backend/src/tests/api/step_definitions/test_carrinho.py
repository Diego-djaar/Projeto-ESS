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

@scenario(scenario_name="Remover um produto de um carrinho", feature_name="..//features/carrinho.feature")
def test_remove_item():
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

@given(parsers.cfparse('um produto com ID "{id}" está no carrinho de CPF "{CPF}"'), target_fixture="context")
def adicionar_item_ao_carrinho(context, id: str, CPF: str):
    context["id"] = id
    context["CPF"] = CPF
    send_get_cart_request(context)
    adiciona_produto_ao_carrinho(context, id)
    return context

@when(parsers.cfparse('o cliente tenta remover o produto com ID "{id}" do carrinho'), target_fixture="context")
def remover_item_do_carrinho(context, id: str):
    response = TESTCLIENT.delete("/carrinho/remover", params={"CPF": context["CPF"], "item_id": id})
    context["response"] = response
    return context

@then(parsers.cfparse('o carrinho de CPF "{CPF}" está vazio'), target_fixture="context")
def empty_cart(context, CPF):
    send_get_cart_request(context)
    check_response_json(context)
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
    context['id'] = id 
    return context

@then(parsers.cfparse('o item deve estar no carrinho'), target_fixture="context")
def verificar_item_no_carrinho(context):
    response = Carrinho_service.get_cart(context["CPF"])
    cart_dict = response.data # Da forma {"Itens": list[DadosItem], "Total": "29.99", "Endereço": "Endereço não registrado"}

    # Obter lista de IDs dos itens no carrinho
    item_ids_no_carrinho = [item.id for item in cart_dict["Itens:"]]

    assert context["id"] in item_ids_no_carrinho
    return context

@when(parsers.cfparse('uma requisição GET for enviada para "/carrinho/view/123.456.789-10"'), target_fixture="context")
def send_get_cart_request(context, client = TESTCLIENT):
    response = client.get(url="/carrinho/view/123.456.789-10")
    context["response"] = response
    return context

@then(
    parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context"
)
def check_response_status_code(context, status_code: int):
    assert context["response"].status_code == int(status_code)
    return context

@then(
    parsers.cfparse('o resultado do JSON deve ser "{expected_data}"'),
    target_fixture="context"
)
def check_response_json(context):
    expected_data = {"Itens:": [], "Total": "0.00", "Endereço": "Endereço não registrado"}
    assert context["response"].json()["data"] == expected_data
    return context