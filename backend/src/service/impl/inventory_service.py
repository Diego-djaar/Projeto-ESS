from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.item_service_meta import ItemServiceMeta
#from src.db.__init__ import ItemDatabase
#from src.db.__init__ import InventoryDatabase
from src.db.itens_database import DadosItem, Item, ItemDatabase
from src.db.inventory_database import InventoryEntryData, InventoryEntry, InventoryDatabase
from src.schemas.item_database_response import HTTPItemDatabaseResponses 
from src.schemas.inventory_response import HTTPItemResponses
from pydantic import BaseModel

class InventoryService(ItemServiceMeta):

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
        inventory_entry = InventoryDatabase.get_inventory_entry_by_ID(item_id)
        if (inventory_entry.cnpj != store_id):
            return HttpResponseModel(
                message=HTTPItemResponses.UNAUTHORIZED().message,
                status_code=HTTPItemResponses.UNAUTHORIZED().status_code,
            )
        # tudo certo
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=item,
            )

    # pegar todos os itens da loja - ok
    @staticmethod
    def get_items(cnpj : str) -> HttpResponseModel:

        # busca 
        allitems = ItemDatabase.get_itens_list()

        storeitems = []

        # entre todos os itens
        for item in allitems: 
            id_item = item.id  # 
            inventory_entry =  InventoryDatabase.get_inventory_entry_by_ID(id_item)  # InventoryEntry correspondente a item
            id_loja = inventory_entry.cnpj  # loja daquele item
            if (id_loja == cnpj):
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
    
    # adicionar item à db itens e à db inventory
    @staticmethod
    def add_new_item(item_data: DadosItem, cnpj : str):
        """Tenta adicionar um novo item no banco de dados"""
        (item, reason) = Item.new_item(*item_data.model_dump().values())
        if item is None:
            return HTTPItemDatabaseResponses.BAD_REQUEST(reason)
        (success, reason) = ItemDatabase.add_new_item(item=item)

        if success:
            
            # add entrada relacionando item à loja
            inventory_entry = InventoryEntry.new_inventory_entry(cnpj = cnpj, id_item = item.id)
            InventoryDatabase.add_new_inventory_entry(inventory_entry)

            # retorna
            return HTTPItemDatabaseResponses.ADD_ITEM_SUCCESSFULLY()
        else:
            return HTTPItemDatabaseResponses.ITEM_ALREADY_EXISTS(reason)

    # remove da db itens e da db inventory
    @staticmethod
    def remove_item(item_id: str) -> HttpResponseModel:
        item = ItemDatabase.remove_item_by_ID(item_id= item_id)
        if item is None:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )

        # remove entrada da base Inventory também
        InventoryDatabase.remove_inventory_entry_by_ID(id_item = item_id)

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