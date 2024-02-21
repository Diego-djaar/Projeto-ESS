from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.carrinho_service import Carrinho_service
from src.schemas.response import HttpResponseModel, HTTPResponses
from src.schemas.carrinho_response import HTTPCarrinhoResponses
from fastapi.testclient import TestClient
from src.main import app
import pytest
from src.db.__init__ import cart_database
from src.db.itens_database import Item
from src.db.carrinho_database import Carrinho

TESTCLIENT = TestClient(app)

import pytest

@pytest.fixture(autouse=True)
def clean_database():
    # Código para limpar a base de dados antes de cada teste
    cart_database.clear_cart_database()

@scenario(scenario_name="Criar carrinho", feature_name="..//features/carrinho.feature")
def test_create_cart():
    pass

@scenario(scenario_name="Adicionar item ao carrinho", feature_name="..//features/carrinho.feature")
def test_add_item_to_cart():
    pass

@scenario(scenario_name="Remover item de carrinho", feature_name="../features/carrinho.feature")
def test_remove_item_from_cart():
    pass

@scenario(scenario_name="Alterar endereço do carrinho", feature_name="../features/carrinho.feature")
def test_modify_adress():
    pass

@given(parsers.cfparse('o carrinho não possui endereço registrado'), target_fixture="context")
def assert_no_adress(context):
    assert context["carrinho"].endereço is None
    return context

@when(parsers.cfparse('adiciona-se o endereço "{endereço}"'), target_fixture="context")
def modify_adress(context, endereço: str):
    endereço_separado = endereço.split(", ")
    carrinho = context["carrinho"]
    carrinho.alterar_endereço(*endereço_separado)
    context["carrinho"] = carrinho
    return context

@then(parsers.cfparse('o carrinho possui endereço "{endereço}"'), target_fixture="context")
def assert_adress(context, endereço: str):
    carrinho = context["carrinho"]
    endereço_formatado = endereço.replace("\\n", "\n")
    assert carrinho.endereço.__str__() == endereço_formatado
    return context

@given(parsers.cfparse('o carrinho possui o item de id "{id}"'), target_fixture="context")
def item_no_carrinho(context, id: str):
    add_item_to_cart(context, id)
    return context

@when(parsers.cfparse('remove-se um item de id "{id}" do carrinho'), target_fixture="context")
def remove_item_from_cart(context, id: str):
    carrinho = context["carrinho"]
    carrinho.remove_item_by_ID(id)
    context["carrinho"] = carrinho
    return context

@then(parsers.cfparse('O carrinho está vazio'), target_fixture="context")
def carrinho_vazio(context):
    carrinho = context["carrinho"]
    assert carrinho.items == {}
    return context

@given(parsers.cfparse('um carrinho de CPF "{CPF}" já foi criado'), target_fixture="context")
def carrinho_criado(context, CPF: str):
    context = criar_carrinho(context, CPF)
    return context

@when(parsers.cfparse('adiciona-se um item de id "{id}" ao carrinho'), target_fixture="context")
def add_item_to_cart(context, id: str):
    item, reason = Item.new_item(id, "nome", "description", "20.99", 1, "imagem.jpg")
    context["item"] = item
    carrinho = context["carrinho"]
    carrinho.add_item(item)
    context["carrinho"] = carrinho
    return context

@then(parsers.cfparse('o carrinho possui o item de id "{id}"'), target_fixture="context")
def item_in_cart(context, id):
    carrinho = context["carrinho"]
    item = context["item"]
    assert item.id in carrinho.items.keys()
    return context

@when(parsers.cfparse('é criado um novo carrinho com os dados (CPF="{CPF}")'), target_fixture="context")
def criar_carrinho(context, CPF: str):
    carrinho = Carrinho(CPF)
    context["carrinho"] = carrinho
    return context

@then(parsers.cfparse('a criação do carrinho é bem sucedida'), target_fixture="context")
def verify_cart_creation(context):
    assert type(context["carrinho"]) == Carrinho
    return context

@then(parsers.cfparse('o carrinho possui os dados (CPF="{CPF}", items={itens}, total="{total}", endereço=None)'), target_fixture="context")
def assert_cart_content(context, CPF: str, itens: dict, total: str, adress: str | None = None):
    assert context["carrinho"].CPF == CPF
    assert str(context["carrinho"].items) == itens
    assert context["carrinho"].total == total
    assert context["carrinho"].endereço == adress
    return context