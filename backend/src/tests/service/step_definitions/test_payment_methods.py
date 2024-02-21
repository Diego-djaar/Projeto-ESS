from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.db.payment_database import * 
from pytest_bdd import given, when, then, scenario, parsers
from datetime import *
import pytest
from bcrypt import hashpw, checkpw, gensalt
import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.payment_schema import Cartao
from src.schemas.payment_response import HTTPPaymentResponse
from src.service.impl.payment_method_service import PaymentService
import src.service.impl.payment_method_service

@scenario(scenario_name="Inserir cartão", feature_name="../features/payment_methods-service.feature")
def testar_cadastro_bem_sucedido():
    pass


@scenario(scenario_name="Inserir cartão com cpf inválido", feature_name="../features/payment_methods-service.feature")
def testar_cadastro_com_cpf_invalido():
    pass


@scenario(scenario_name="Inserir cartão fora da validade", feature_name="../features/payment_methods-service.feature")
def testar_cadastro_fora_validade():
    pass


@scenario(scenario_name="Inserir cartão fora da validade", feature_name="../features/payment_methods-service.feature")
def testar_cadastro_fora_validade():
    pass


@scenario(scenario_name="Inserir cartão com numero inválido", feature_name="../features/payment_methods-service.feature")
def testar_cadastro_numero_invalido():
    pass


@scenario(scenario_name="Inserir pix", feature_name="../features/payment_methods-service.feature")
def testar_cadastro_pix():
    pass


@then(parsers.cfparse('o cartao de número "{numero}" e cpf "{cpf}" não existe no banco de dados'))
@given(parsers.cfparse('o cartao de número "{numero}" e cpf "{cpf}" não existe no banco de dados'))

def checar_cartao_nao_existe(numero: str, cpf: str):

    assert get_card_by_number_and_cpf(numero, cpf) is None 


@then(parsers.cfparse('o cartao de número "{numero}" e cpf "{cpf}" existe no banco de dados'))
@given(parsers.cfparse('o cartao de número "{numero}" e cpf "{cpf}" existe no banco de dados'))

def checar_cartao_existe(numero: str, cpf: str):

    assert get_card_by_number_and_cpf(cpf, numero) is not None 


@given(parsers.cfparse('o pix de nome "{nome}" e cpf "{cpf}" não existe no banco de dados'))

def checar_existencia_pix(nome: str, cpf: str): 

    assert get_pix_by_cpf(cpf) is None 

@then(parsers.cfparse('o pix de nome "{nome}" e cpf "{cpf}" existe no banco de dados'))
@given(parsers.cfparse('o pix de nome "{nome}" e cpf "{cpf}" existe no banco de dados'))

def checar_nao_existencia_pix(nome: str, cpf: str): 

    assert get_pix_by_cpf(cpf) is not None 


@when(parsers.cfparse('o método inserting_card do PaymentMethodService for chamado com Cartao nome "{nome}", número "{numero}", cvv "{cvv}", cpf "{cpf}" e validade "{validade}"')
      , target_fixture="response")

def inserir_cartao(nome: str, numero: str, cvv: str, cpf: str, validade: datetime): 

    data_datetime = datetime.datetime.strptime(validade.strip('""'), "%Y-%m-%d").date()

    cartao = src.service.impl.payment_method_service.Cartao(
        nome_cartao=nome, 
        numero_cartao=numero,
        cvv= cvv, 
        cpf = cpf, 
        validade= data_datetime
    )

    return src.service.impl.payment_method_service.PaymentService.inserting_card(cartao)


@when(parsers.cfparse('o método insert_pix do PaymentDatabase for chamado com Pix nome "{nome}" e cpf "{cpf}"'), target_fixture="response")

def inserir_pix(nome: str, cpf: str):

    pix =  src.service.impl.payment_method_service.Pix(
        nome_completo=nome, 
        cpf = cpf, 
    )

    return src.service.impl.payment_method_service.PaymentService.insertion_pix(pix)


@then(parsers.cfparse('o metodo insert_pix retorna uma mensagem de confirmação para o pix de cpf {cpf}'))

def verificar_mensagem_resposta(response, cpf: str): 

    id = get_pix_id(cpf)

    res: HttpResponseModel = response
    assert res == HTTPPaymentResponse.INSERTION_SUCESSFULLY(id)


@then(parsers.cfparse('o metodo insert_card retorna uma mensagem de confirmação para o cartao de número "{numero}" e cpf "{cpf}"'))

def checar_retorno_cartao(response, numero: str, cpf: str):

    id = get_cartao_id(cpf, numero)

    res: HttpResponseModel = response
    assert res == HTTPPaymentResponse.INSERTION_SUCESSFULLY(id)


@then(parsers.cfparse('o metodo insert_card retorna uma mensagem de insucesso para o cartao de nome "{nome_cartao}", número "{numero}", cvv "{cvv}" e cpf "{cpf}" e validade "{validade}"'))

def checar_retorno_insucesso_cartao(response, nome_cartao: str, numero: str, cvv: str, cpf: str, validade: str): 

    data_datetime = datetime.datetime.strptime(validade.strip('""'), "%Y-%m-%d").date()

    sucesso, problemas = insert_card(nome_cartao, numero, cvv, cpf, data_datetime)

    res: HttpResponseModel = response
    assert res == HTTPPaymentResponse.BAD_REQUEST(problemas)



