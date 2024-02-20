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
    def get_item(item_id: str, cnpj : str) -> HttpResponseModel:

        # busca direto em inventário
        entry = InventoryDatabase.get_inventory_entry_by_ID(id_item: str)
        if entry is None:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        # se existe mas não é da loja
        else if entry.cnpj != cnpj:
            return HttpResponseModel(
                message=HTTPItemResponses.UNAUTHORIZED().message,
                status_code=HTTPItemResponses.UNAUTHORIZED().status_code,
            )
        # tudo certo
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=entry,
            )


    @staticmethod
    def get_items(cnpj : str) -> HttpResponseModel:
        # busca 
        all_entries = InventoryDatabase.get_inventory_list()

        valid_entries = []

        # entre todos os itens
        for entry in all_entries: 
            if (entry.cnpj == cnpj):
                valid_entries.append(entry)

        if storeitems.__len__() == 0:
            return HttpResponseModel(
                message=HTTPItemDatabaseResponses.NO_ITEM_IN_DATABASE().message,
                status_code=HTTPItemDatabaseResponses.NO_ITEM_IN_DATABASE().status_code,
            )

        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=valid_entries
            )
    
    # adicionar item à db itens e à db inventory
    @staticmethod
    def add_new_item(item_data: DadosItem, cnpj : str, qnt : int):
        """Tenta adicionar um novo item no banco de dados"""

        (item, reason) = Item.new_item(*item_data.model_dump().values())
        
        if item is None:
            return HTTPItemDatabaseResponses.BAD_REQUEST(reason)
        (success, reason) = ItemDatabase.add_new_item(item=item)

        if success:
            
            # add valores na db inventário
            inventory_entry = InventoryEntry.new_inventory_entry(cnpj = cnpj, id_item = item.id, nome = item.nome, qnt = qnt)
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
    

    @staticmethod
    def modify_item_quantity(item_id: str, qnt : int) -> HttpResponseModel:
        """Troca unicamente quantidade. para trocar outros atributos, usar itens_database_service"""
        (success, reason) = InventoryDatabase.modify_inventory_entry_quantity(item_id = item_id, qnt = qnt)

        if success:
            return HTTPDatabaseResponses.MODIFY_ITEM_SUCCESSFULLY()
        else:
            return HTTPItemDatabaseResponses.BAD_REQUEST(reason)