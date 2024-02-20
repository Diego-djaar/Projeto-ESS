from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.item_service_meta import ItemServiceMeta
#from src.db.__init__ import ItemDatabase
#from src.db.__init__ import LojaItemDatabase
from src.db.itens_database import DadosItem, Item, ItemDatabase
from src.db.store_item_database import DadosLojaItem, LojaItem, LojaItemDatabase
from src.schemas.item_database_response import HTTPItemDatabaseResponses
from src.schemas.store_item_response import HTTPLojaItemResponses
from pydantic import BaseModel


class LojaItemService(ItemServiceMeta):

    # ------------------------------------------------------------------------------------
    def ITEM_ALREADY_EXISTS(reason_list: list[str]) -> HttpResponseModel:

    def NO_ITEM_IN_DATABASE() -> HttpResponseModel:

    def BAD_REQUEST(reason_list: list[str]) -> HttpResponseModel:

    def ADD_ITEM_SUCCESSFULLY() -> HttpResponseModel:

    def REMOVE_ITEM_SUCCESSFULLY() -> HttpResponseModel:

    def MODIFY_ITEM_SUCCESSFULLY() 
    # ----------------------------------------------------------------------------------
    @staticmethod
    def get_item(item_id: str, store_id : str) -> HttpResponseModel:
        item = ItemDatabase.get_item_by_ID(item_id= item_id)
        # se não existe:
        if item is None:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        # se existe mas não é da loja
        lojaitem = LojaItemDatabase.get_lojaitem_by_ID(item_id)
        if (lojaitem.id_loja != store_id):
            return HttpResponseModel(
                message=HTTPLojaItemResponses.UNAUTHORIZED().message,
                status_code=HTTPLojaItemResponses.UNAUTHORIZED().status_code,
            )
        # tudo certo
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=item,
            )

    # pegar todos os itens da loja - ok
    @staticmethod
    def get_items(id_loja : str) -> HttpResponseModel:

        # busca 
        allitems = ItemDatabase.get_itens_list()

        storeitems = []

        # entre todos os itens
        for item in allitems: 
            id_item = item.id  # 
            lojaitem =  LojaItemDatabase.get_lojaitem_by_ID(id_item)  # LojaItem correspondente a item
            loja = lojaitem.id_loja  # loja daquele item
            if (loja == id_loja):
                storeitems.append(item) # adiciona à lista retornada apenas se for da loja que estiver pedindo

        if storeitems.__len__() == 0:
            return HttpResponseModel(
                message=HTTPItemDatabaseResponses.NO_ITEM_IN_DATABASE().message,
                status_code=HTTPItemDatabaseResponses.NO_ITEM_IN_DATABASE().status_code,
            )

        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=storeitems,
            )
    
    # adicionar item à db itens e à db lojas-itens
    @staticmethod
    def add_new_item(item_data: DadosItem, id_loja : str):
        """Tenta adicionar um novo item no banco de dados"""
        (item, reason) = Item.new_item(*item_data.model_dump().values())
        if item is None:
            return HTTPItemDatabaseResponses.BAD_REQUEST(reason)
        (success, reason) = ItemDatabase.add_new_item(item=item)

        if success:
            
            # add entrada relacionando item à loja
            lojaitem = LojaItem.new_lojaitem(id_loja = id_loja, id_item = item.id)
            LojaItemDatabase.add_new_lojaitem(lojaitem)

            # retorna
            return HTTPItemDatabaseResponses.ADD_ITEM_SUCCESSFULLY()
        else:
            return HTTPItemDatabaseResponses.ITEM_ALREADY_EXISTS(reason)

    # remove da db itens e da db lojas-itens
    @staticmethod
    def remove_item(item_id: str) -> HttpResponseModel:
        item = ItemDatabase.remove_item_by_ID(item_id= item_id)
        if item is None:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )

        # remove entrada da base lojas-itens também
        LojaItemDatabase.remove_lojaitem_by_ID(id_item = item_id)

        return HttpResponseModel(
                message=HTTPItemDatabaseResponses.REMOVE_ITEM_SUCCESSFULLY().message,
                status_code=HTTPItemDatabaseResponses.REMOVE_ITEM_SUCCESSFULLY().status_code,
                data=item,
            )
    
    # esse fica igual: troca atributos do item, não troca loja à qual pertence
    @staticmethod
    def modify_item(item_id: str, new_item_data: DadosItem) -> HttpResponseModel:
        """Tenta modificar um item do banco de dados. Na prática só associa os novos dados do item ao id do alvo."""
        (item, reason) = Item.new_item(*new_item_data.model_dump().values())
        if item is None:
            return HTTPItemDatabaseResponses.BAD_REQUEST(reason)
        (success, reason) = ItemDatabase.modify_item_by_ID(item_id= item_id, new_item=item)
        if success:
            return HTTPDatabaseResponses.MODIFY_ITEM_SUCCESSFULLY()
        else:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )