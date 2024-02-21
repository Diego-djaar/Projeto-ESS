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
    store_database.add_store(Store.new("121212", "@loja.com", "htft8", "alimento", "Hortifruti"))




@scenario(scenario_name="Recuperação de senha", feature_name="../features/store_update.feature")
def test_successeful_password_retrieval():
    pass

@given(parsers.cfparse('Loja "{nome}", de CNPJ "{cnpj}" já está cadastrada com senha "{senha}"'))
def verify_store_not_db(context, cnpj: str): 
    assert store_database.get_store_by_cnpj(cnpj) is not None


@when(parsers.cfparse('Uma requisição {request_type} for enviada para "{store_retrieve_pass}", com as seguintes informações (CNPJ: "{cnpj}", Email: "{email}", Nova_senha: "{nsenha}")'), target_fixture="context",)
def retrieve_request(request_type: str, store_retrieve_pass: str, cnpj: str , nsenha: str, email: str, client=TESTCLIENT):
    retrieval_request = {
        "cnpj": cnpj,
        "email": email,
        "nsenha": nsenha
    }

    post_= getattr(client, request_type.lower())
    return post_("/backend/api/stores/" + store_retrieve_pass, json=retrieval_request)


@then(parsers.cfparse('o status da resposta deve ser "{status}"'))
def check_status(status: str, context):
    assert int(status) == context.status_code


@then(parsers.cfparse('o campo "{campo}" tem o resultado negativo "{message}"'))
def check_good_message(context):
    context_json = context.json()
    assert context_json['detail'] == "CNPJ ou Email incorretos"





@scenario(scenario_name="Recuperação de senha com dados incorretos", feature_name="../features/store_update.feature")
def test_failed_password_retrieval():
    pass

@given(parsers.cfparse('Loja "{nome}", de CNPJ "{cnpj}" já está cadastrada com senha "{senha}"'))
def verify_store_not_db(context, cnpj: str): 
    assert store_database.get_store_by_cnpj(cnpj) is not None


@when(parsers.cfparse('Uma requisição {request_type} for enviada para "{store_retrieve_pass}", com as seguintes informações (CNPJ: "{cnpj}", Email: "{email}", Nova_senha: "{nsenha}")'), target_fixture="context",)
def retrieve_request(request_type: str, store_retrieve_pass: str, cnpj: str , nsenha: str, email: str, client=TESTCLIENT):
    retrieval_request = {
        "cnpj": cnpj,
        "email": email,
        "nsenha": nsenha
    }

    post_= getattr(client, request_type.lower())
    return post_("/backend/api/stores/" + store_retrieve_pass, json=retrieval_request)


@then(parsers.cfparse('o status da resposta deve ser "{status}"'))
def check_status(status: str, context):
    assert int(status) == context.status_code

@then(parsers.cfparse('A senha da loja de CNPJ "{cnpj}" agora é "{senha}"'))
def check_password(cnpj: str, senha: str,  context):
    assert store_database.get_store_by_cnpj(cnpj).senha == senha


@then(parsers.cfparse('o campo "{campo}" tem o resultado positivo "{message}"'))
def check_good_message(context):
    context_json = context.json()
    assert context_json['message'] == "Atualização de dados bem sucedida"






@scenario(scenario_name="Modificação de dados de uma loja", feature_name="../features/store_update.feature")
def test_success_change_data():
    pass

@given(parsers.cfparse('Loja "{nome}", de CNPJ "{cnpj}" já está cadastrada com senha "{senha}"'))
def verify_store_not_db(context, cnpj: str): 
    assert store_database.get_store_by_cnpj(cnpj) is not None


@when(parsers.cfparse('Uma requisição {request_type} for enviada para "{store_change_data}", com as seguintes informações (CNPJ: "{cnpj}", Senha: "{senha}", novoNome: "{nNome}", novaCategoria: "{nCategoria}", novoEmail: "{nEmail}")'), target_fixture="context",)
def retrieve_request(request_type: str, store_change_data: str, cnpj: str , senha: str, nNome: str, nCategoria: str, nEmail: str, client=TESTCLIENT):
    change_data_request = {
        "cnpj": cnpj,
        "nemail": nEmail,
        "senha": senha,
        "nsenha": senha,
        "ncategoria": nCategoria,
        "nnome": nNome,
    }

    post_= getattr(client, request_type.lower())
    return post_("/backend/api/stores/" + store_change_data, json=change_data_request)


@then(parsers.cfparse('o status da resposta deve ser "{status}"'))
def check_status(status: str, context):
    assert int(status) == context.status_code

@then(parsers.cfparse('A categoria da loja de CNPJ "{cnpj}" é atualizada para "{nCategoria}"'))
def check_password(cnpj: str, nCategoria: str,  context):
    assert store_database.get_store_by_cnpj(cnpj).categoria == nCategoria

@then(parsers.cfparse('O nome da loja de CNPJ "{cnpj}" é atualizado para "{nNome}"'))
def check_password(cnpj: str, nNome: str,  context):
    assert store_database.get_store_by_cnpj(cnpj).nome == nNome


@then(parsers.cfparse('o campo "{campo}" tem o resultado "{message}"'))
def check_good_message(context):
    context_json = context.json()
    assert context_json['message'] == "Atualização de dados bem sucedida"
