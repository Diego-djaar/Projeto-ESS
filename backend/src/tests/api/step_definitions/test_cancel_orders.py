from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.db.orders_db import *
from pytest_bdd import parsers, given, when, then, scenario
import datetime
import pytest
from src.main import app

TESTCLIENT = TestClient(app)

@pytest.fixture(autouse=True)
def change_db():
    db = {}
    orders_database = read_file(db, "orders.json")

    for order in orders_database["111.222.333-44"]:
        if order["id"] == 1:
            order["_status"] = "On the way"
            order["cancel_reason"] = None
    
    write_file(orders_database, "orders.json")

"""Scenario: Cancelar pedidos com sucesoso"""
@scenario(scenario_name="Cancelar pedido com sucesso", feature_name="../features/cancel_orders.feature")
def test_cancel_orders():
    """Processa pedido de cancelamento"""

"""Scenario: Cancelar pedidos já entregues mal sucedido"""
@scenario(scenario_name="Cancelar pedido já entregue mal sucedido", feature_name="../features/cancel_orders.feature")
def test_cancel_orders_delivered():
    """Processa pedido de cancelmento já entregue mal sucedido"""

"""Scenario: Cancelar pedidos já entregues mal sucedido"""
@scenario(scenario_name="Cancelar pedido já cancelado mal sucedido", feature_name="../features/cancel_orders.feature")
def test_cancel_orders_canceled():
    """Processa pedido de cancelmento já cancelado mal sucedido"""

@given(parsers.cfparse('o usuário de CPF "{user_cpf}" possui o produto de ID "{product_id}" e de status "{product_status}" atrelado a ele'))
def verify_product_status_on_the_way(user_cpf: str, product_id: int, product_status:str):
    db = {}
    orders_database = read_file(db, "orders.json")

    found_product = None
    for order in orders_database[user_cpf]:
        if order["id"] == int(product_id):
            found_product = order
            break

    if found_product:
        real_product_status = found_product["_status"]
        assert real_product_status == product_status

@given(parsers.cfparse('o usuário de CPF "{user_cpf}" possui o produto de ID "{product_id}" e de status "{product_status}" atrelado a ele'))
def verify_product_status_delivered(user_cpf: str, product_id: int, product_status:str):
    db = {}
    orders_database = read_file(db, "orders.json")

    found_product = None
    for order in orders_database[user_cpf]:
        if order["id"] == int(product_id):
            found_product = order
            break

    if found_product:
        real_product_status = found_product["_status"]
        assert real_product_status == product_status

@given(parsers.cfparse('o usuário de CPF "{user_cpf}" possui o produto de ID "{product_id}" e de status "{product_status}" atrelado a ele'))
def verify_product_status_canceled(user_cpf: str, product_id: int, product_status:str):
    db = {}
    orders_database = read_file(db, "orders.json")

    found_product = None
    for order in orders_database[user_cpf]:
        if order["id"] == int(product_id):
            found_product = order
            break

    if found_product:
        real_product_status = found_product["_status"]
        assert real_product_status == product_status

@when(parsers.cfparse('é solicitado uma requisição "{request_type}" para cancelar pedido com dados ID do produto "{product_id}", CPF do usuário "{user_cpf}" e razão do cancelamento "{cancel_reason}"'), target_fixture= "request_response")
def cancel_request(
    request_type: str, 
    product_id: int,
    user_cpf: str,
    cancel_reason: str, 
    client=TESTCLIENT
):
    cancel_request = {
        "product_id": product_id,
        "user_cpf": user_cpf,
        "cancel_reason": cancel_reason
    }

    post = getattr(client, request_type.lower())
    return post(f"/backend/api/orders/cancel/{product_id}?user_CPF={user_cpf}&cancel_reason={cancel_reason}", json=cancel_request)

@then(parsers.cfparse('o status de resposta deverá ser de "{response_status}"'))
def check_response_status(response_status: str, request_response):
    assert int(response_status) == request_response.status_code

@then(parsers.cfparse('a mensagem de resposta deverá conter o produto foi cancelado com sucesso'))
def check_succesfuly_response_msg(request_response):
    request_response_json = request_response.json()
    assert request_response_json['message'] == 'Pedido cancelado com sucesso!'

@then(parsers.cfparse('a mensagem de resposta deverá conter que o produto já foi entregue'))
def check_delivery_response_msg(request_response):
    request_response_json = request_response.json()
    assert request_response_json['message'] == 'O pedido já foi entregue!'

@then(parsers.cfparse('a mensagem de resposta deverá conter que o produto já foi cancelado'))
def check_canceled_response_msg(request_response):
    request_response_json = request_response.json()
    assert request_response_json['message'] == 'O pedido já foi cancelado!'