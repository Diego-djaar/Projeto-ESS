from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.carrinho_service import Carrinho_service
from src.schemas.response import HttpResponseModel, HTTPResponses
from src.schemas.carrinho_response import HTTPCarrinhoResponses
from fastapi.testclient import TestClient
from src.main import app
import pytest
from src.db.__init__ import cart_database
from src.db.itens_database import Item

TESTCLIENT = TestClient(app)

import pytest

@pytest.fixture(autouse=True)
def clean_database():
    # Código para limpar a base de dados antes de cada teste
    cart_database.clear_cart_database()


@scenario(scenario_name= "Obter carrinho por CPF", feature_name="..//features/carrinho.feature")
def test_get_cart_by_CPF():
    pass

@scenario(scenario_name="Adicionar um produto válido ao carrinho", feature_name="..//features/carrinho.feature")
def test_add_valid_product_to_cart():
    pass

@scenario(scenario_name="Remover um produto de um carrinho", feature_name="..//features/carrinho.feature")
def test_remove_item():
    pass

@scenario(scenario_name="Falha em remover um produto de um carrinho vazio", feature_name="..//features/carrinho.feature")
def test_remove_item_from_empty_cart():
    pass

@scenario(scenario_name="Limpar conteúdo do carrinho", feature_name="..//features/carrinho.feature")
def test_clear_cart_content():
    pass

@scenario(scenario_name="Limpar a base de dados de carrinhos", feature_name="..//features/carrinho.feature")
def test_clear_cart_database_content():
    pass

@scenario(scenario_name="Incrementar quantidade de um item no carrinho", feature_name="..//features/carrinho.feature")
def test_increment_item_quantity():
    pass

@scenario(scenario_name="Decrementar quantidade de um item no carrinho com quantidade maior que 1", feature_name="..//features/carrinho.feature")
def test_decrementar_item_com_quantidade_maior_que_1():
    pass

@scenario(scenario_name="Decrementar quantidade de um item no carrinho com quantidade 1", feature_name="..//features/carrinho.feature")
def test_decrementar_item_com_quantidade_1():
    pass

@scenario(scenario_name="Alterar endereço de destino do pedido", feature_name="..//features/carrinho.feature")
def test_alterar_endereço():
    pass

@given(parsers.cfparse('o endereço do carrinho de CPF "{CPF}" não foi registrado'), target_fixture="context")
def endereço_nao_registrado(context, CPF: str):
    context["CPF"] = CPF
    send_get_cart_request(context)
    check_response_json(context)
    return context

@when(parsers.cfparse('o endereço do carrinho de CPF "{CPF}" é alterado para "{endereço}"'), target_fixture="context")
def alterar_endereço(context, CPF: str, endereço: str):
    endereco_lista = endereço.split(", ")
    print(type(context))
    response = TESTCLIENT.put("/backend/api/carrinho/alterar_endereço", params={"CPF": CPF}, json={
        "rua": endereco_lista[0],
        "numero": endereco_lista[1],
        "bairro": endereco_lista[2],
        "cidade": endereco_lista[3],
        "estado": endereco_lista[4],
        "cep": endereco_lista[5],
        "pais": endereco_lista[6],
        "complemento": endereco_lista[7]
    })
    print(f'{context} CONTEXT')
    print(type(context))
    context["response"] = response
    return context

@then(parsers.cfparse('o carrinho de CPF "{CPF}" tem "{endereço}" no campo endereço'), target_fixture="context")
def assert_adress(context, CPF: str, endereço: str):
    send_get_cart_request(context)
    print(context["response"].json()['data']['Endereço'])
    print(endereço)
    endereço_carrinho = context['response'].json()['data']["Endereço"]
    endereço_carrinho_formatado = endereço_carrinho.replace("\\n", "\n")
    endereço_formatado = endereço.replace("\\n", "\n")
    print(endereço_formatado)
    assert endereço_carrinho_formatado == endereço_formatado
    return context

@given(parsers.cfparse('o Carrinho_service retorna um carrinho com cpf "{CPF_}"'))
def mock_cart_service_response(CPF_: str):
    #Carrinho_service.get_cart = lambda CPF: HttpResponseModel(
    #    message=HTTPResponses.ITEM_FOUND().message,
    #    status_code=HTTPResponses.ITEM_FOUND().status_code,
    #    data={"Itens:": {}, "Total": "0.00", "Endereço": "Endereço não registrado"}
    #)
    pass

@given(parsers.cfparse('um produto com ID "{id}" está disponível'))
def produto_disponivel(id: str):
    # Adicionar lógica para verificar se o produto está disponível na base de dados
    pass

@given(parsers.cfparse('o carrinho do cliente com CPF "{CPF_}" está vazio'), target_fixture="context")
def carrinho_vazio(context, CPF_: str):
    # Inicialização do carrinho
    context['CPF'] = CPF_
    response = TESTCLIENT.get(url="/backend/api/carrinho/view/123.456.789-10")
    assert response.status_code == 200
    return context

@given(parsers.cfparse('um produto com ID "{id}" está no carrinho de CPF "{CPF_}"!'), target_fixture="context")
def adicionar_item_ao_carrinho(context, id: str, CPF_: str):
    context["id"] = id
    context["CPF"] = CPF_
    send_get_cart_request(context)
    adiciona_produto_ao_carrinho(context, id)
    return context

@given(parsers.cfparse('os produtos com ID "{id1}" e "{id2}" estão no carrinho de CPF "{CPF_}"'), target_fixture="context")
def carrinho_com_dois_itens(context, id1: str, id2: str, CPF_: str):
    context["CPF"] = CPF_
    send_get_cart_request(context)
    adiciona_produto_ao_carrinho(context, id1)
    adiciona_produto_ao_carrinho(context, id2)
    return context

@given(parsers.cfparse('os carrinhos de CPF "{CPF1}", "{CPF2}" e "{CPF3}" estão registrados'), target_fixture="context")
def registrar_carrinhos(context, CPF1: str, CPF2: str, CPF3: str):
    context["CPF"] = CPF1
    send_get_cart_request(context)
    context["CPF"] = CPF2
    send_get_cart_request(context)
    context["CPF"] = CPF3
    send_get_cart_request(context)
    return context

@given(parsers.cfparse('um produto com ID "{ID}" de preço "{preço}" está no carrinho de CPF "{CPF_}" com quantidade "{quantidade}"'), target_fixture="context")
def garantir_condicoes_iniciais(context, ID: str, preço: str, CPF_: str, quantidade: int):
    print("given")
    context["id"] = str(ID)
    context["CPF"] = str(CPF_)
    print(context)
    send_get_cart_request(context)
    assert context["response"].status_code == 200
    adiciona_produto_ao_carrinho(context, id= str(ID), quantidade=int(quantidade), preço=str(preço))
    return context

@when(parsers.cfparse('o item é incrementado'), target_fixture="context")
def incrementar_item(context):
    print("Incrementar item")
    response = TESTCLIENT.put("backend/api/carrinho/incrementar_item",params={"item_id": context["id"], "CPF": context["CPF"]})
    print(context["CPF"])
    print(response.url)
    context["response"] = response
    return context

@when(parsers.cfparse('o item é decrementado'), target_fixture="context")
def decrementar_item(context):
    response = TESTCLIENT.put("backend/api/carrinho/decrementar_item",params={"item_id": context["id"], "CPF": context["CPF"]})
    context["response"] = response
    return context

@then(parsers.cfparse('o produto de ID "{ID}" no carrinho "{CPF_}" deve ter a quantidade "{quantidade}"'), target_fixture="context")
def verify_quantity(context, ID: str, CPF_: str, quantidade: int):
    verificar_item_no_carrinho(context)
    
    # Obter lista de IDs dos itens no carrinho
    cart_dict = context["response"].data
    for item in cart_dict["Itens:"]:
        if item.id == ID:
            assert item.quantidade == int(quantidade)
    
    return context

@then(parsers.cfparse('o total do carrinho de CPF "{CPF_}" é "{total}"'), target_fixture="context")
def verify_total(context, CPF_: str, total: str):
    cart_dict = context["response"].data
    assert cart_dict["Total"] == total
    return context


@when(parsers.cfparse('a base de dados de carrinhos é limpa'), target_fixture="context")
def clear_database(context):
    response = TESTCLIENT.delete("/backend/api/carrinho/clear_carts")
    context["response"] = response
    return context

@then(parsers.cfparse('a base de dados de carrinhos deve estar vazia'))
def verify_clear_database(database = cart_database):
    assert database.db == {}

@when(parsers.cfparse('o carrinho de CPF "{CPF_}" é limpo'), target_fixture="context")
def clear_cart(context, CPF_: str):
    response = TESTCLIENT.delete("/backend/api/carrinho/clear_cart", params= {"CPF": CPF_})
    context["response"] = response
    return context

@when(parsers.cfparse('o cliente tenta remover o produto com ID "{id}" do carrinho'), target_fixture="context")
def remover_item_do_carrinho(context, id: str):
    response = TESTCLIENT.delete("/backend/api/carrinho/remover", params={"CPF": context["CPF"], "item_id": id})
    context["response"] = response
    return context

@then(parsers.cfparse('o carrinho de CPF "{CPF_}" está vazio'), target_fixture="context")
def empty_cart(context, CPF_):
    send_get_cart_request(context)
    check_response_json(context)
    return context


@when(parsers.cfparse('o cliente adiciona o produto com ID "{id}" ao carrinho'), target_fixture="context")
def adiciona_produto_ao_carrinho(context, id: str, quantidade: int = 1, preço: str = "29.99"):
    response = TESTCLIENT.post("/backend/api/carrinho/adicionar", 
                               json={
                                        "id": str(id),
                                        "nome": "Camisa",
                                        "description": "string",
                                        "price": preço,
                                        "quantidade": quantidade,
                                        "img": "string.jpg"
                                    }, 
                                    params={"CPF": context["CPF"]})
    context["response"] = response
    context["id"] = id 
    return context

@then(parsers.cfparse('o item deve estar no carrinho'), target_fixture="context")
def verificar_item_no_carrinho(context):
    response = Carrinho_service.get_cart(context["CPF"])
    cart_dict = response.data # Da forma {"Itens": list[DadosItem], "Total": "29.99", "Endereço": "Endereço não registrado"}

    # Obter lista de IDs dos itens no carrinho
    item_ids_no_carrinho = [item.id for item in cart_dict["Itens:"]]

    assert context["id"] in item_ids_no_carrinho
    context["response"] = response
    return context

@when(parsers.cfparse('uma requisição GET for enviada para "/backend/api/carrinho/view/123.456.789-10"'), target_fixture="context")
def send_get_cart_request(context, client = TESTCLIENT):
    print("send_get_cart_request")
    print(type(context))
    response = client.get(url="/backend/api/carrinho/view/123.456.789-10")
    context["response"] = response
    return context

@then(
    parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context"
)
def check_response_status_code(context, status_code: int):
    assert context["response"].status_code == int(status_code)
    return context

@then(
    parsers.cfparse('o resultado do JSON deve ser "{expected_data}"'),
    target_fixture="context"
)
def check_response_json(context):
    expected_data = {"Itens:": [], "Total": "0.00", "Endereço": "Endereço não registrado"}
    assert context["response"].json()["data"] == expected_data
    return context