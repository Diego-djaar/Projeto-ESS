from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.orders_service import OrdersService
from src.schemas.response import HttpResponseModel
from src.main import app
import pytest
import requests

from src.schemas.orders_response import HTTPOrdersResponse
from fastapi.testclient import TestClient

TESTCLIENT = TestClient(app)

response_data = {"111.222.333-44": [
        {
            "_id": 1,
            "supplier_name": "Fornecedor A",
            "name": "Produto A",
            "img": "XXXX",
            "quantity": 2,
            "price": 10.50,
            "request_date": "2023-12-15",
            "delivery_date": "2023-12-27",
            "delivery_model": "Entrega Expressa",
            "_status": "Entregue",
            "cancel_reason": "",
            "payment_method": "Cartão de Crédito"
        },
        {
            "_id": 2,
            "supplier_name": "Fornecedor B",
            "name": "Produto B",
            "img": "YYYY",
            "price": 20.75,
            "request_date": "2023-12-26",
            "delivery_date": "2023-12-28",
            "delivery_model": "Entrega Padrão",
            "_status": "Processando",
            "cancel_reason": "",
            "payment_method": "Boleto Bancário"
        }
    ]}

@scenario(scenario_name= "Obter pedidos por CPF", feature_name="../features/order_history.feature")
def test_get_orders_by_cpf():
    pass

@scenario(scenario_name= "Usuário quer visualizar um pedido específico", feature_name="../features/order_history.feature")
def test_get_order_by_cpf():
    pass

@scenario(scenario_name="Obter pedidos com determinado Filtro", feature_name="../features/order_history.feature")
def test_history_filter():
    pass
    
@given(parsers.cfparse('o OrdersService retorna uma lista de pedidos que contém os pedidos de ids "{order_1}" e "{order_2}"'))

def mock_orders_service_response(order_1: int, order_2: int):

    OrdersService.orders_user_service = lambda id: HttpResponseModel(
        message= HTTPOrdersResponse.GET_SUCCESSFULLY(response_data[0]).message,
        status_code= HTTPOrdersResponse.GET_SUCCESSFULLY(response_data[0]).status_code,
        data = [order for order in response_data["111.222.333-44"] if order["_id"] in (order_1, order_2)]
    )

@given(parsers.cfparse('o OrdersService retorna uma lista de pedidos filtrados que contém o pedido de id "{order_id}"'))

def mock_orders_filtered_service_response(order_id: int):

    OrdersService.orders_filtered_service = lambda id: HttpResponseModel(
        message= HTTPOrdersResponse.GET_SUCCESSFULLY(response_data[0]).message,
        status_code= HTTPOrdersResponse.GET_SUCCESSFULLY(response_data[0]).status_code,
        data = response_data["111.222.333-44"]["_id" == 1]
    )
@given(parsers.cfparse('a lista de pedidos possui a chave CPF "{cpf}" e possui o pedido de ID "{order_id}" associado a ele'))

def mock_order_service_response(cpf: str, order_id: int):
    assert cpf in response_data
    assert any(order['_id'] == int(order_id) for order in response_data[cpf])


@when(
    parsers.cfparse('uma requisição GET é enviada para "{url}"'),
    target_fixture="request_response"
)
def send_get_orders_request(url: str):
    url = "http://127.0.0.1:8000" + url
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)

    return response

@when(
    parsers.cfparse('é solicitado uma requisição GET para "{url}" com o parâmetro CPF do usuário "{cpf}" e ID de pedido "{order_id}"'),
    target_fixture="request_response"
)
def send_get_orders_request(url: str, cpf: str, order_id : int):
    url = "http://127.0.0.1:8000" + url + cpf + "&" + str(order_id)
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)

    return response

@when(
    parsers.cfparse('uma requisição POST é enviada para "{url}" com o body contendo o CPF "{cpf}", o price_max "{valor}" e o restante dos campos nulos'),
    target_fixture="request_response"
)
def send_get_orders_request(url: str, cpf: str, valor: str):
    url = "http://127.0.0.1:8000" + url
    body = { 
        "cpf": cpf, "id": None, "supplier_name" : None, "name" : None,
        "quantity": None, "price_min": None, "price_max": valor,
        "start_date": None, "end_date": None
    }
    headers = {'accept': 'application/json'}

    response = requests.post(url, headers=headers,json=body)
    print(response.json())

    return response


@then(
    parsers.cfparse('o status de resposta JSON deve ser "{status_code}"')
)
def check_response_status_code(request_response, status_code: int):
    assert int(request_response.status_code) == int(status_code)

@then(
    parsers.cfparse('a mensagem de resposta será "{mensagem}"')
)
def check_response_message(request_response, mensagem: str):
    assert request_response.json()["message"] == mensagem

@then(
    parsers.cfparse('o JSON de resposta deve ser uma lista com um único pedido')
)
def check_list_lenght(request_response):
    orders = request_response.json()
    assert len(orders["data"]) == 1


@then(
    parsers.cfparse('o JSON de resposta deve ser uma lista de pedidos')
)
def check_response_json(request_response):
    orders = request_response.json()['data']
    assert isinstance(orders, list)

    for order in orders:
        assert isinstance(order, dict)
        assert "_id" in order and isinstance(order["_id"], int)

@then(
    parsers.cfparse('o pedido de id "{order_id}" e nome "{order_name}" está na lista')
)
def check_order_in_list(request_response, order_id: int, order_name: str):
    orders = request_response.json()["data"]
    assert any(order['_id'] == int(order_id) and order["name"] == order_name for order in orders)

@then(
    parsers.cfparse('o JSON de resposta terá os dados do pedido "{order_id}"')
)
def check_order_in_list(request_response, order_id: int):
    order = request_response.json()["data"]
    assert order["_id"] == int(order_id)
