from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.db.payment_database import * 
from pytest_bdd import parsers, given, when, then, scenario
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

@given(parsers.cfparse(
    'o cartao de número {numero} e cpf {cpf} não existe no banco de dados'
))

def testar_cartao_nao_existe(numero: str, cpf: str):

    assert get_card_by_number_and_cpf(numero, cpf) is None 

@when(parsers.cfparse(
    'o método inserting_card do PaymentMethodService for chamado com Cartao nome {nome}, número {numero}, cvv {cvv}, cpf {cpf} e validade {validade}'
), target_fixture="signup_response" )

def inserir_cartao(nome: str, numero: str, cvv: str, cpf: str, validade: datetime): 

    # data_datetime = datetime.datetime.strptime(validade.strip('""'), "%Y-%m-%d").date()

    cartao = src.service.impl.payment_method_service.Cartao(
        nome_cartao=nome, 
        numero_cartao=numero,
        cvv= cvv, 
        cpf = cpf, 
        validade= validade
    )

    return src.service.impl.payment_method_service.PaymentService.inserting_card(cartao)

@then(parsers.cfparse(
    'o metodo insert_card retorna uma mensagem de confirmação para o cartao de número {numero} e cpf {cpf}'
))

def checar_retorno(signup_response, numero: str, cpf: str):

    id = get_cartao_id(cpf, numero)

    res: HttpResponseModel = signup_response
    assert res["data"]["ID"] == HTTPPaymentResponse.INSERTION_SUCESSFULLY(id)["data"]["ID"]

