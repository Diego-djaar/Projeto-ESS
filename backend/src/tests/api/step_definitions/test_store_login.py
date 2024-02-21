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
    store_database.add_store(Store.new("37.565.457/0001-90", "htft@gmail", "htft8", "alimentos", "Hortifruti"))




@scenario(scenario_name="Login de loja já cadastrada", feature_name="../features/store_login.feature")
def test_successeful_login():
    pass

@given(parsers.cfparse('Loja "{nome}", de CNPJ "{cnpj}" já está cadastrada com senha "{senha}"'))
def verify_store_not_db(context, cnpj: str): 
    assert store_database.get_store_by_cnpj(cnpj) is not None


@when(parsers.cfparse('Uma requisição {request_type} for enviada para "{store_login}", com as seguintes informações (CNPJ: "{cnpj}", Senha: "{senha}")'), target_fixture="context",)
def login_request(request_type: str, store_login: str, cnpj: str ,senha: str, client=TESTCLIENT):
    login_request = {
        "cnpj": cnpj,
        "senha": senha,
    }

    post_= getattr(client, request_type.lower())
    return post_("/backend/api/stores/" + store_login, json=login_request)


@then(parsers.cfparse('o status da resposta deve ser "{status}"'))
def check_status(status: str, context):
    assert int(status) == context.status_code

@then(parsers.cfparse('o campo "{campo}" tem o resultado positivo "{message}"'))
def check_good_message(context):
    context_json = context.json()
    assert context_json['message'] == "Login com sucesso"





@scenario(scenario_name="Tentativa de Login com senha incorreta", feature_name="../features/store_login.feature")
def test_wrong_pass_login():
    pass

@given(parsers.cfparse('Loja "{nome}", de CNPJ "{cnpj}" já está cadastrada com senha "{senha}"'))
def verify_store_not_db(context, cnpj: str): 
    assert store_database.get_store_by_cnpj(cnpj) is not None


# @when(parsers.cfparse('Uma requisição {request_type} for enviada para "{store_login}", com as seguintes informações (CNPJ: "{cnpj}", Senha: "{senha}")'), target_fixture="context",)
# def login_request(request_type: str, store_login: str, cnpj: str ,senha: str, client=TESTCLIENT):
#     login_request = {
#         "cnpj": cnpj,
#         "senha": senha,
#     }

#     post_= getattr(client, request_type.lower())
#     return post_("/backend/api/stores/" + store_login, json=login_request)


# @then(parsers.cfparse('o status da resposta deve ser "{status}"'))
# def check_status(status: str, context):
#     assert int(status) == context.status_code

@then(parsers.cfparse('o campo "{campo}" tem o resultado negativo "{message}"'))
def check_good_message(context):
    context_json = context.json()
    assert context_json['detail'] == "CNPJ ou Senha incorretos"





@scenario(scenario_name="Login de loja não cadastrada", feature_name="../features/store_login.feature")
def test_failed_login():
    pass

@given(parsers.cfparse('Loja "{nome}", de CNPJ "{cnpj}" não está cadastrada'))
def verify_store_not_db(context, cnpj: str): 
    assert store_database.get_store_by_cnpj(cnpj) is None


# @when(parsers.cfparse('Uma requisição {request_type} for enviada para "{store_login}", com as seguintes informações (CNPJ: "{cnpj}", Senha: "{senha}")'), target_fixture="context",)
# def login_request(request_type: str, store_login: str, cnpj: str ,senha: str, client=TESTCLIENT):
#     login_request = {
#         "cnpj": cnpj,
#         "senha": senha,
#     }

#     post_= getattr(client, request_type.lower())
#     return post_("/backend/api/stores/" + store_login, json=login_request)


# @then(parsers.cfparse('o status da resposta deve ser "{status}"'))
# def check_status(status: str, context):
#     assert int(status) == context.status_code

@then(parsers.cfparse('o campo "{campo}" tem o resultado "{message}"'))
def check_good_message(context):
    context_json = context.json()
    assert context_json['detail'] == "Login falhou, essa loja não deve estar cadastrada"