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