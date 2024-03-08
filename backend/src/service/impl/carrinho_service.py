from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.__init__ import cart_database as db
from src.db.carrinho_database import Carrinho, Carrinhos
from src.db.itens_database import Item
from src.schemas.item_database_response import HTTPDatabaseResponses
from pydantic import BaseModel
from src.schemas.carrinho_response import HTTPCarrinhoResponses
from src.db.itens_database import DadosItem

class DadosEndereço(BaseModel):
    rua: str
    numero: int
    bairro: str
    cidade: str
    estado: str
    cep: str
    pais: str
    complemento: str | None

class Carrinho_service():

    @staticmethod
    def get_cart(CPF: str, database: Carrinhos = db) -> HttpResponseModel:
        """ Tenta obter um carrinho, se não conseguir criar um novo para o CPF selecionado """
        print("Entrou em get_cart")
        carrinho = database.get_cart_by_CPF(CPF= CPF)
        if carrinho is None:
            print("Entrou em carrinho is none")
            carrinho = Carrinho(CPF=CPF)
            (success, reason) = database.add_new_cart(carrinho)
            item_list = [item.to_dados_item() for item in carrinho.get_all_items()]
            return HttpResponseModel(
                message="Carrinho não encontrado, novo carrinho criado vinculado a este CPF",
                status_code=HTTPResponses.ITEM_CREATED().status_code,
                data={"Itens": item_list, "Total": carrinho.total, "Endereço": carrinho.get_adress()},
            )
        item_list = [item.to_dados_item() for item in carrinho.get_all_items()]
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data={"Itens": item_list, "Total": carrinho.total, "Endereço": carrinho.get_adress()},
            )

    @staticmethod
    def get_all_carts(database: Carrinhos = db) -> HttpResponseModel:
        cart_database = database.get_cart_list()
        # cart_database é uma lista de objetos do tipo Carrinho. Transformar em um dicionário de cpf: {"Itens": lista de itens,"Total": total}
        cart_dict = dict()
        for carrinho in cart_database:
            lista_itens = carrinho.get_all_items()
            carrinho_formatado = {"Itens": lista_itens, "Total": carrinho.total}
            cart_dict[carrinho.CPF] = carrinho_formatado
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=cart_dict,
            )
    
    @staticmethod
    def add_item_to_cart(item_data: DadosItem, CPF: str, database: Carrinhos = db):
        """Tenta adicionar um novo item no banco de dados"""
        print("Entrou em add_item_to_cart")
        print(item_data)
        item_data_dict = item_data.model_dump()  # Se isso retornar um dicionário com as chaves corretas
        (item, reason) = Item.new_item(**item_data_dict)
        if item is None:
            print("Entrou item is None")
            return HTTPDatabaseResponses.BAD_REQUEST(reason)
        (success, reason) = database.add_item_to_cart(item=item, CPF= CPF)

        if success:
            return HTTPDatabaseResponses.ADD_ITEM_SUCCESSFULLY()
        else:
            return HTTPCarrinhoResponses.CART_NOT_FOUND()

    @staticmethod
    def remove_item_from_cart(item_id: str, CPF: str, database: Carrinhos = db) -> HttpResponseModel:
        (success, reason) = database.remove_item_from_cart(item_id= item_id, CPF= CPF)
        if not success:
            return HttpResponseModel(
                message=reason[0],
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        return HttpResponseModel(
                message=HTTPDatabaseResponses.REMOVE_ITEM_SUCCESSFULLY().message,
                status_code=HTTPDatabaseResponses.REMOVE_ITEM_SUCCESSFULLY().status_code,
            )
    
    @staticmethod
    def decrease_item_quantity(item_id: str, CPF: str, database: Carrinhos = db) -> HttpResponseModel:
        """Tenta remover um na quantidade do item no carrinho"""
        (success, reason) = database.decrease_item_quantity(item_id=item_id, CPF=CPF)
        if not success:
            return HttpResponseModel(
                message=reason[0],
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        return HTTPCarrinhoResponses.DECREASE_ITEM_QUANTITY(reason[0])
    
    @staticmethod
    def increase_item_quantity(item_id: str, CPF: str, database: Carrinhos = db) -> HttpResponseModel:
        """Tenta adicionar um na quantidade do item no carrinho"""
        (success, reason) = database.increase_item_quantity(item_id= item_id, CPF= CPF)
        if not success:
            return HttpResponseModel(
                message=reason[0],
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code
            )
        return HTTPCarrinhoResponses.MODIFY_ITEM_QUANTITY()
    
    @staticmethod
    def clear_cart_by_CPF(CPF: str, database: Carrinhos = db) -> HttpResponseModel:
        """ Tenta limpar um carrinho da base de dados """
        print("Entrou em clear_cart_by_CPF")
        success = database.clear_cart_by_CPF(CPF=CPF)
        return HTTPCarrinhoResponses.CLEAR_CART(success)
    
    @staticmethod
    def clear_all_carts(database: Carrinhos = db) -> HttpResponseModel:
        database.clear_cart_database()
        return HTTPCarrinhoResponses.CLEAR_ALL_CARTS()
    
    @staticmethod
    def add_adress(adressData: DadosEndereço, CPF: str, database: Carrinhos = db) -> HttpResponseModel:
        adressData_dict = adressData.model_dump()  # Se isso retornar um dicionário com as chaves corretas
        (success, reason) = database.alterar_endereco_de_carrinho_por_CPF(CPF, **adressData_dict)
        if success:
            return HTTPCarrinhoResponses.MODIFY_ADRESS_SUCCESFULLY()
        return HTTPCarrinhoResponses.CART_NOT_FOUND()