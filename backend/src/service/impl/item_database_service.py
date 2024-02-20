from schemas.response import HTTPResponses, HttpResponseModel
from service.meta.item_service_meta import ItemServiceMeta
from db.__init__ import ItemDatabase as db
from db.itens_database import Item, ItemDatabase
from schemas.item_database_response import HTTPDatabaseResponses
from pydantic import BaseModel

class DadosItem(BaseModel):
    id: str # Acessos a database serão pelo ID (8 dígitos)
    nome: str # Nome visível na interface
    description: str
    price: str
    quantidade: int
    img: str | None # Path para o arquivo

class ItemService(ItemServiceMeta):

    @staticmethod
    def get_item(item_id: str) -> HttpResponseModel:
        item = ItemDatabase.get_item_by_ID(item_id= item_id)
        if item is None:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=item,
            )

    @staticmethod
    def get_items() -> HttpResponseModel:
        items = ItemDatabase.get_itens_list()
        if items.__len__() == 0:
            return HttpResponseModel(
                message=HTTPDatabaseResponses.NO_ITEM_IN_DATABASE().message,
                status_code=HTTPDatabaseResponses.NO_ITEM_IN_DATABASE().status_code,
            )

        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=items,
            )
    
    @staticmethod
    def add_new_item(item_data: DadosItem, database = db):
        """Tenta adicionar um novo item no banco de dados"""
        (item, reason) = Item.new_item(*item_data.model_dump().values())
        if item is None:
            return HTTPDatabaseResponses.BAD_REQUEST(reason)
        (success, reason) = db.add_new_item(item=item)

        if success:
            return HTTPDatabaseResponses.ADD_ITEM_SUCCESSFULLY()
        else:
            return HTTPDatabaseResponses.ITEM_ALREADY_EXISTS(reason)

    @staticmethod
    def remove_item(item_id: str) -> HttpResponseModel:
        item = ItemDatabase.remove_item_by_ID(item_id= item_id)
        if item is None:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        return HttpResponseModel(
                message=HTTPDatabaseResponses.REMOVE_ITEM_SUCCESSFULLY.message,
                status_code=HTTPDatabaseResponses.REMOVE_ITEM_SUCCESSFULLY.status_code,
                data=item,
            )
    
    @staticmethod
    def modify_item(item_id: str, new_item_data: DadosItem) -> HttpResponseModel:
        """Tenta modificar um item do banco de dados. Na prática só associa os novos dados do item ao id do alvo."""
        (item, reason) = Item.new_item(*new_item_data.model_dump().values())
        if item is None:
            return HTTPDatabaseResponses.BAD_REQUEST(reason)
        (success, reason) = ItemDatabase.modify_item_by_ID(item_id= item_id, new_item=item)
        if success:
            return HTTPDatabaseResponses.MODIFY_ITEM_SUCCESSFULLY()
        else:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
