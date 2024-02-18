from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.item_service_meta import ItemServiceMeta
from src.db.__init__ import cart_database as db
from src.db.carrinho_database import Carrinho, Carrinhos
from src.db.itens_database import Item
from src.schemas.item_database_response import HTTPDatabaseResponses
from pydantic import BaseModel
from src.schemas.carrinho_response import HTTPCarrinhoResponses

class DadosItem(BaseModel):
    id: str # Acessos a database serão pelo ID (8 dígitos)
    nome: str # Nome visível na interface
    description: str
    price: str
    quantidade: int
    img: str | None # Path para o arquivo

class Carrinho_service():

    @staticmethod
    def get_cart(CPF: str, database: Carrinhos = db) -> HttpResponseModel:
        """ Tenta obter um carrinho, se não conseguir criar um novo para o CPF selecionado """
        carrinho = database.get_cart_by_CPF(CPF= CPF)
        if carrinho is None:
            carrinho = Carrinho(CPF=CPF)
            (success, reason) = database.add_new_cart(carrinho)
            if not success:
                return HttpResponseModel(
                    message=reason[0],
                    status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
                )
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=carrinho.items,
            )

    @staticmethod
    def get_all_carts(database: Carrinhos = db) -> HttpResponseModel:
        cart_database = database.get_cart_list()
        # cart_database é uma lista de objetos do tipo Carrinho. Transformar em um dicionário de cpf: lista de itens
        cart_dict = dict()
        for carrinho in cart_database:
            cart_dict[carrinho.CPF] = carrinho.get_all_items()
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=cart_dict,
            )
    
    @staticmethod
    def add_item_to_cart(item_data: DadosItem, CPF: str, database: Carrinhos = db):
        """Tenta adicionar um novo item no banco de dados"""
        print(item_data)
        item_data_dict = item_data.model_dump()  # Se isso retornar um dicionário com as chaves corretas
        (item, reason) = Item.new_item(**item_data_dict)
        if item is None:
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
        success = database.clear_cart_by_CPF(CPF=CPF)
        return HTTPCarrinhoResponses.CLEAR_CART(success)
    
    @staticmethod
    def clear_all_carts(database: Carrinhos = db) -> HttpResponseModel:
        database.clear_cart_database()
        return HTTPCarrinhoResponses.CLEAR_ALL_CARTS()