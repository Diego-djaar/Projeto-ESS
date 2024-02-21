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
        "nome_cartao": "MasterCard",
        "numero_cartao": "4916123456789012",
        "cvv": "375",
        "cpf": "111.111.111-11",
        "validade": "2028-10-08"
    }

    existing_card = get_card_by_number_and_cpf(card_info["cpf"], card_info["numero_cartao"])

    if existing_card is not None:
        remove_card(card_info["cpf"], card_info["numero_cartao"])

"Cenário: Cadastrar cartao de credito válido"
@scenario(scenario_name="Cadastrar cartão de crédito válido", feature_name="../features/insert_card-api.feature")    

def testar_cadastro_cartao_valido(): 
    pass 

"Cenário: Cadastrar cartão de crédito com cpf inválido"
@scenario(scenario_name="Cadastrar cartão de crédito com cpf inválido", feature_name="../features/insert_card-api.feature") 

def testar_cadastro_cartao_cpf_incorreto(): 
    pass 


@given(parsers.cfparse('o cartao de nome "{nome}", numero "{numero}", cvv "{cvv}", cpf "{cpf}" e validade "{validade}" não está cadastrado'))
@then(parsers.cfparse('o cartao de nome "{nome}", numero "{numero}", cvv "{cvv}", cpf "{cpf}" e validade "{validade}" não está cadastrado'))

def verificar_cartao_nao_existente(nome: str, numero: str, cvv: str, cpf: str, validade: datetime.date): 

    assert get_card_by_number_and_cpf(cpf, numero) is None 

@then(parsers.cfparse('O cartao de nome "{nome}", numero "{numero}", cvv "{cvv}", cpf "{cpf}" e validade "{validade}" está cadastrado'))
@given(parsers.cfparse('O cartao de nome "{nome}", numero "{numero}", cvv "{cvv}", cpf "{cpf}" e validade "{validade}" está cadastrado'))
def verificar_cartao_existente(numero: str, cpf: str):
    

    assert get_card_by_number_and_cpf(cpf, numero) is not None 

@when(
    parsers.cfparse('uma requisição "{request_type}" foi enviada para "{insert_card}" com Cartao(nome_cartao "{nome}", numero_cartao "{numero}", cvv "{cvv}", cpf "{cpf}" e validade "{validade}")'),
    target_fixture="request_response"
)
def enviar_requisicao(request_type: str, insert_card: str, nome: str, numero: str, cvv: str, cpf: str, validade: datetime.date, client=TESTCLIENT):



    insert_card_request = {
    "nome_cartao": nome,
    "numero_cartao": numero,
    "cvv": cvv,
    "cpf": cpf,
    "validade": validade
    }
    
    post_ = getattr(client, request_type.lower())
    return post_("/backend/src/api/payment/inserting/cartao", json=insert_card_request)

@when(parsers.cfparse("a requisição está correta"))

def assert_correction():
    """A requisição deve estar correta
    
    Não é necessário checar aqui
    """
    pass

@when(parsers.cfparse('o campo de "{campo}" de requisição é validado'))
def validade_field():
    """O campo deve ser validado
    
    Não é necessário checar aqui
    """
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

@then("o JSON da resposta indica que o campo validade foi mal preenchido")
def check_response_unsucessfull_json_validade(request_response): 
    request_response_json = request_response.json()
    assert request_response_json["data"][1] == "VALIDADE"

@then("o JSON da resposta indica que o campo numero_cartao foi mal preenchido")
def check_response_unsucessfull_json_numero_cartao(request_response): 
    request_response_json = request_response.json()
    assert request_response_json["data"][2] == "CARD_NUMBER"

@then('o JSON da resposta indica que a atualização foi bem sucedido')
def check_update_response_json(request_reponse): 
    request_reponse_json = request_reponse.json()
    assert request_reponse_json["message"] == "Dados atualizados com sucesso"