from fastapi.testclient import TestClient
from src.db.__init__ import store_database
from src.db.store_database import Store
from pytest_bdd import parsers, given, when, then, scenario
import pytest
from src.main import app
import json

TESTCLIENT = TestClient(app)

@pytest.fixture(autouse=True)
def remove_test_from_db():
    store_database.remove_store_by_cnpj("48.449.992/0001-65")
    store_database.add_store(Store.new("36.565.457/0001-90", "vitor@gmail", "123", "alimentos", "lojalegal"))




@scenario(scenario_name="Cadastro bem sucedido", feature_name="../features/store_signup.feature")
def test_successeful_signup():
    pass

@given(parsers.cfparse('Loja "{nome}", de CNPJ "{cnpj}" não está cadastrada'))
def verify_store_not_db(context, cnpj: str): 
    assert store_database.get_store_by_cnpj(cnpj) is None


@when(parsers.cfparse('Uma requisição {request_type} for enviada para "{store_signup}", com as seguintes informações (Nome: "{nome}", CNPJ: "{cnpj}", Email: "{email}", Senha: "{senha}", Categoria: "{categoria}")'), target_fixture="context",)
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

    post_= getattr(client, request_type.lower())
    return post_("/backend/api/stores/" + store_signup, json=signup_request)



@then(parsers.cfparse('o status da resposta deve ser "{status}"'))
def check_status(status: str, context):
    assert int(status) == context.status_code

@then(parsers.cfparse('o campo "{campo}" tem o resultado positivo "{message}"'))
def check_good_message(context):
    context_json = context.json()
    assert context_json['message'] == "Loja cadastrada com sucesso"






@scenario(scenario_name="Tentativa de cadastro de loja já cadastrada", feature_name="../features/store_signup.feature")
def test_failed_signup():
    pass


@given(parsers.cfparse('Loja "{nome}", de CNPJ "{cnpj}" já está cadastrada'))
def verify_store_in_db(cnpj: str):
    assert store_database.get_store_by_cnpj(cnpj) is not None


# @when(parsers.cfparse('Uma requisição {request_type} for enviada para "{store_signup}", com as seguintes informações (Nome: "{nome}", CNPJ: "{cnpj}", Email: "{email}", Senha: "{senha}", Categoria: "{categoria}")'), target_fixture="context",)
# def signup_request(request_type: str, store_signup: str
#                    , nome: str, cnpj: str
#                    , email: str, senha: str, categoria: str, client=TESTCLIENT):
#     signup_request = {
#         "nome": nome,
#         "cnpj": cnpj,
#         "email": email,
#         "senha": senha,
#         "categoria": categoria,
#     }

#     post_= getattr(client, request_type.lower())
#     return post_("/backend/api/stores/" + store_signup, json=signup_request)



# @then(parsers.cfparse('o status da resposta deve ser "{status}"'))
# def check_status(status: str, context):
#     assert int(status) == context.status_code


@then(parsers.cfparse('O campo "{campo}" tem o resultado negativo "{message}"'))
def check_negative_message(context):
    context_json = context.json()
    print(context_json)
    assert context_json['detail'] == "Já existe uma loja registrada com esses dados"
    









