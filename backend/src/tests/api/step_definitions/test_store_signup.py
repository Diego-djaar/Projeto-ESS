from fastapi.testclient import TestClient
from src.db.__init__ import store_database
from src.db.store_database import Store
from pytest_bdd import parsers, given, when, then, scenario
import pytest
from src.main import app
import json

TESTCLIENT = TestClient(app)

@scenario(scenario_name="Cadastro bem sucedido", feature_name="../features/store_signup.feature")
def test_successelful_signup():
    pass

@given(parsers.cfparse('Loja "{nome}", de CNPJ "{cnpj}" não está cadastrada'))
def verify_store_not_db(cnpj: str):
    assert store_database.get_store_by_cnpj(cnpj) is None

@when(parsers.cfparse('Uma requisição {request_type} for enviada para "{store_signup}", com as seguintes informações (Nome: "{nome}", CNPJ: "{cnpj}", Email: "{email}", Senha: "{senha}", Categoria: "{categoria}")'), target_fixture="request_response")
def signup_request(request_type: str, store_signup: str
                   , nome: str, cnpj: str
                   , email: str, senha: str, categoria: str, client=TESTCLIENT):
    signup_request = {
        "nome": nome,
        "cnpj": cnpj,
        "email": email,
        "senha": senha,
        "categoria": categoria,
    }

    post = getattr(client, request_type.lower())
    return post("/backend/api/user/" + store_signup, json=signup_request)


@then(parsers.cfparse('o status da resposta deve ser "{status}"'))
def check_status(status: str, request_response):
    assert int(status) == request_response.status_code

@then(parsers.cfparse('o campo "{campo}" tem o valor "{message}"'))
def check_message(request_response):
    request_response_json = request_response.json()
    assert request_response_json['message'] == "Loja cadastrada com sucesso"

