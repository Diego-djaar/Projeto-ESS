from schemas.response import HTTPResponses, HttpResponseModel
from service.meta.item_service_meta import ItemServiceMeta
#from db.__init__ import ItemDatabase
#from db.__init__ import InventoryDatabase
from db.itens_database import DadosItem, Item, ItemDatabase
from db.inventory_database import InventoryEntryData, InventoryEntry, InventoryDatabase
from db.__init__ import inventory_database as db
from db.__init__ import item_database as item_db
from schemas.item_database_response import HTTPDatabaseResponses 
from schemas.inventory_response import HTTPItemResponses
from pydantic import BaseModel


class InventoryService(ItemServiceMeta):


    @staticmethod
    def get_item(item_id: str, cnpj : str) -> HttpResponseModel:

        # busca direto em inventário
        entry = db.get_inventory_entry_by_ID(id_item)
        if entry is None:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        # se existe mas não é da loja
        elif entry.cnpj != cnpj:
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

    # todas as entradas referentes àquele cnpj
    @staticmethod
    def get_items(cnpj : str) -> HttpResponseModel:
        # busca 
        entries = db.get_inventory_list_by_cnpj(cnpj = cnpj)

        print(entries)

        if entries.__len__() == 0:
            return HttpResponseModel(
                message=HTTPDatabaseResponses.NO_ITEM_IN_DATABASE().message,
                status_code=HTTPDatabaseResponses.NO_ITEM_IN_DATABASE().status_code,
            )

        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=entries
            )
    
    # adicionar item à db itens e à db inventory
    @staticmethod
    def add_new_item_service(item_data: DadosItem, cnpj : str, qnt : int):
        """Tenta adicionar um novo item no banco de dados"""

        (item, reason) = Item.new_item(*item_data.model_dump().values())
        
        if item == None:
            return HTTPDatabaseResponses.BAD_REQUEST(reason)
        (success, reason) = item_db.add_new_item(item=item)
	
        if success:
            
            # add valores na db inventário
            (inventory_entry, reason ) = InventoryEntry.new_inventory_entry(cnpj = cnpj, id_item = item.id, nome = item.nome, qnt = qnt)
            db.add_new_inventory_entry(inventory_entry)

            # retorna
            return HTTPDatabaseResponses.ADD_ITEM_SUCCESSFULLY()
        else:
            return HTTPDatabaseResponses.ITEM_ALREADY_EXISTS(reason)

    # remove da db itens e da db inventory
    @staticmethod
    def remove_item(item_id: str) -> HttpResponseModel:
        item = item_db.remove_item_by_ID(item_id= item_id)
        if item is None:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )

        # remove entrada da base Inventory também
        db.remove_inventory_entry_by_ID(id_item = item_id)

        return HttpResponseModel(
                message=HTTPDatabaseResponses.REMOVE_ITEM_SUCCESSFULLY().message,
                status_code=HTTPDatabaseResponses.REMOVE_ITEM_SUCCESSFULLY().status_code,
                data=item,
            )
    
    @staticmethod
    def modify_item_quantity(item_id: str, qnt : int) -> HttpResponseModel:
        """Troca unicamente quantidade. para trocar outros atributos, usar itens_database_service"""
        (success, reason) = db.modify_inventory_entry_quantity(item_id = item_id, qnt = qnt)

        if success:
            return HTTPDatabaseResponses.MODIFY_ITEM_SUCCESSFULLY()
        else:
            return HTTPDatabaseResponses.BAD_REQUEST(reason)
