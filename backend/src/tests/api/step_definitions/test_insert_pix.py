from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.db.payment_database import * 
from pytest_bdd import parsers, given, when, then, scenario
import datetime
import pytest
from src.main import app

TESTCLIENT = TestClient(app)

@pytest.fixture(autouse=True)

def remover_card_from_database():

    card_info = {
        "nome_completo": "Breno Gabriel de Melo Lima",
        "cpf": "111.111.111-11"
    }

    existing_pix =get_pix_by_cpf(card_info["cpf"])

    if existing_pix is not None:
        remove_card(card_info["cpf"], card_info["numero_cartao"])

@scenario(scenario_name="Cadastrar pix válido", feature_name="../features/insert_pix-api.feature")
def test_cadastro_pix_valido():
    pass 

"""Scenario: Cadastrar pix com cpf inválido"""
@scenario(scenario_name="Cadastrar pix com cpf inválido", feature_name="../features/insert_pix-api.feature")
def testar_cadastro_pix_invalido():
    pass

@given(parsers.cfparse('o pix de cpf "{cpf}" e nome "{nome}" não está cadastrado na base de dados'))

def testar_existencia_na_base_dados(cpf: str, nome: str):

    assert get_pix_by_cpf(cpf) is None 

@then(parsers.cfparse('o pix de cpf "{cpf}" e nome "{nome}" está cadastrado na base de dados'))
@given(parsers.cfparse('o pix de cpf "{cpf}" e nome "{nome}" está cadastrado na base de dados'))

def testar_nao_existencia_na_base_dados(cpf: str, nome: str):

    assert get_pix_by_cpf(cpf) is not None 

@when(parsers.cfparse(
    'uma requisição "{requisicao}" for enviada para "{rota}", com Pix(nome "{nome}", cpf "{cpf}")'
), target_fixture="request_response")

def enviar_requisicao(requisicao: str, rota: str, nome: str, cpf: str, client=TESTCLIENT):

    insert_pix = {
    "nome_cartao": nome,
    "cpf": cpf,
    }
    
    post_ = getattr(client, requisicao.lower())
    return post_("/backend/src/api/payment/inserting/cartao", json=insert_pix)

@when(parsers.cfparse(
    'a requisição está correta'
))

def checar_requisicao(): 

    pass 

@then(parsers.cfparse(
    'o campo "{campo}" da requisição é validado'
))

def verificar_campo():
    pass 

@then(parsers.cfparse('o status da resposta deve ser "{status}"'))
def check_response_status(status: str, request_response):
    assert int(status) == request_response.status_code

@then('o JSON da resposta indica que o cadastro foi bem sucedido')
def check_response_sucessfull_json(request_response):
    request_response_json = request_response.json()
    assert request_response_json['message'] == "metodo de pagamento cadastrado com sucesso"

@then("o JSON da resposta indica que o cadastro foi mal sucedido")
def check_response_unsucessfull_json(request_response): 
    request_response_json = request_response.json()
    assert request_response_json["message"] == "informações inválidas"

@then("o JSON da resposta indica que o campo CPF foi mal preenchido")
def check_response_unsucessfull_json_cpf(request_response): 
    request_response_json = request_response.json()
    assert request_response_json["data"][0] == "CPF"
