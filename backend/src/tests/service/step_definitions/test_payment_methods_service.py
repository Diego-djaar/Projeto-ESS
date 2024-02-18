
# from pytest_bdd import parsers, given, when, then, scenario
# from src.db.payment_database import *
# from src.service.impl.payment_method_service import PaymentService 
# from src.schemas.response import HttpResponseModel, HTTPResponses
# from src.schemas.payment_schema import * 
# import typing
# import datetime


# @scenario(feature_name="../features/payment_methods-service.feature", 
#           scenario_name="Inserir cartão")

# def test_payment_method_service():
#     pass

# # @given(parsers.cfparse(
# #     'o cartao de nome {nome}, número {numero}, cvv {cvv}, cpf {cpf} e validade {validade} não existe no banco de dados'
# # ))

# # def checar_nao_existencia(numero): 



# @given(parsers.cfparse(
#     'o método inserting_card do PaymentMethodService retorna um json com message {mensagem} e status_code = {status}'
# ))

# def mock_insert_service(mensagem: str, status: int ):

#     PaymentService.inserting_card = lambda id: HttpResponseModel(
#         message=mensagem, 
#         status_code=status
#     )

# @when(parsers.cfparse(
#     'o método inserting_card do PaymentMethodService for chamado com cartao {cartao}'
# ), target_fixture = "context")

# def insertion_card(context, cartao: Cartao):
#     context["result"] = PaymentService.inserting_card(cartao)
#     print(context)
#     return context

# @then(parsers.cfparse(
#     'o método inserting_card do PaymentMethodService retorna um json com message "método cadastrado com sucesso" e status_code = "201"', 
# ), target_fixture = "context")
# def check_response(context, sucesso_esperado: bool, problemas_esperados: List[str]):

#     sucesso_retornado, problemas_retornados = context["result"]

#     sucesso_retornado = str(sucesso_retornado)
#     problemas_esperados = str(problemas_esperados)

#     assert bool(sucesso_retornado) == bool(sucesso_esperado)
#     assert problemas_retornados == json.loads(problemas_esperados.replace("'", '"'))

#     return context

from src.main import app
from unittest.mock import MagicMock
from unittest.mock import patch
from fastapi.testclient import TestClient
from src.db import database as db
from datetime import datetime, timezone
from unittest.mock import patch, MagicMock
from src.service.impl.payment_method_service import PaymentService
from src.schemas.payment_schema import *

def test_add_card(client: TestClient):

    mock_json = {
        "message": "metodo de pagamento cadastrado com sucesso", 
        "status_code": 201, 
        "data": None
    }

    body = {
        "nome_cartao": "MasterCard",
        "numero_cartao": "6011234567890123",
        "cvv": "456",
        "cpf": "111.111.111-11",
        "validade": "2024-02-18"
        }
    
    PaymentService.inserting_card = MagicMock(return_value = mock_json)

    response = client.post("/backend/src/api/payment/inserting/cartao", json=body)

    assert response.status_code == 201 
    assert response.json() ==  {
        "message": "metodo de pagamento cadastrado com sucesso", 
        "status_code": 201, 
        "data": None
    }

