from typing import List, Dict
from uuid import uuid4
from pymongo import MongoClient, errors
from pymongo.collection import Collection, IndexModel
#from config.config import env
from logging import INFO, WARNING, getLogger
from decimal import Decimal
import re
import os.path
import jsonpickle
from pydantic import BaseModel

class InventoryEntryData(BaseModel):
    cnpj: str # id de 14 dígitos
    id_item: str # id de 8 dígitos
    qnt : int # quantidade: número inteiro
    nome : str # nome do item

logger = getLogger('uvicorn')

class InventoryEntry():
    """Classe que associa uma loja com um item e uma quantidade
    
        Criar com método new_inventory_entry()

    Returns:
        (Item, "SUCCESS"), ou (None, reason) caso o input não seja validado.
        
        reason será o nome do campo rejeitado pela validação
    """

    cnpj: str # 14 dígitos
    id_item: str # id de 8 dígitos
    qnt : int # quantidade
    nome : str
    CNPJ_LENGTH = 14  # CNPJ
    ID_ITEM_LENGTH = 8

    def __init__(self, cnpj: str, id_item: str, qnt: int, nome: str):
        self.cnpj = cnpj
        self.id_item = id_item
        self.qnt = qnt
        self.nome = nome
    
    def inventory_entry_to_data(self):
        return InventoryEntryData(
            cnpj = self.cnpj,
            id_item = self.id_item,
            qnt = self.qnt,
            nome = self.nome
        )
    
    @staticmethod
    def new_inventory_entry(cnpj: str, id_item: str, qnt : int, nome : str):
        """Cria nova entrada no inventário a menos que excessão seja levantada

        Args:
            cnpj: str
            id_item : str
            qnt: int
            nome: str

        Returns:
            (InventoryEntry, "SUCCESS"), ou (None, reason) caso o input não seja validado.
            
            reason será a lista dos campos rejeitados pela validação. ["SUCCESS"] caso seja validado.
        """

        reason = []
        
        # Verifica se ID item tem 8 dígitos
        if str(id_item).__len__() != InventoryEntry.ID_ITEM_LENGTH:
            reason.append("ID item com tamanho inválido")

        # Verifica se ID loja tem 14 dígitos (CNPJ)
        if str(cnpj).__len__() != InventoryEntry.CNPJ_LENGTH:
            reason.append("CNPJ deve ter 14 dígitos")

        # Verifica se quantidade é não negativa
        if qnt < 0:
            reason.append("Quantidade deve ser não negativa")

        # verifica que nome é não nulo
        if nome == "":
            reason.append("Nome deve ser não nulo")

        obj = None
        if reason.__len__() == 0:
            reason.append("SUCCESS")
            obj = InventoryEntry(cnpj = cnpj, id_item = id_item, qnt = qnt, nome = nome)

        return (obj, reason)
        

class InventoryDatabase():
    db: dict[InventoryEntry]
    file_path:str

    def __init__(self, path: str = "Inventory.json"):
        self.db = dict()
        self.file_path = path
        self.try_read_from_file()

    def try_read_from_file(self):
        # Ler itens do arquivo
        if not os.path.exists(self.file_path):
            self.write_to_file()
            return None

        with open(self.file_path) as file:
            itens = file.read()
            db = jsonpickle.decode(itens)
            if type(db) == dict:
                self.db = db
    
    def write_to_file(self):
        objetos = jsonpickle.encode(self.db)
        with open(self.file_path, 'w+') as file:
            file.write(objetos)
    
    def get_inventory_list(self):
        """Retorna todos as entradas da base"""
        self.try_read_from_file()
        return list(self.db.values())
    
    def add_new_inventory_entry(self, inventory_entry: InventoryEntry):
        """Adicionar um novo objeto InventoryEntry à base

        Args:
            inventory_entry (InventoryEntry)

        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            reason (list[str]): contém "InventoryEntry com mesmo ID já na base de dados" se for um item já existente.
            ["SUCCESS"] caso tenha sido uma operação bem sucedida
        """
        reason = []
        self.try_read_from_file()
        # verifica id do item, porque id da loja pode ocorrer mais de uma vez
        if InventoryDatabase.get_inventory_entry_by_ID(inventory_entry.id_item):
            reason.append("InventoryEntry com mesmo ID já na base de dados")
        
        if reason.__len__() > 0:
            return (False, reason)
        
        # chave é id do item
        self.db[inventory_entry.id_item] = inventory_entry
        self.write_to_file()
        return (True, ["SUCCESS"])


    def modify_inventory_entry_quantity(self, item_id : str, qnt : int):
        """modifica InventoryEntry na base

        Args:
            inventory_entry (InventoryEntry)


        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            reason (list[str]): contém "Chave inexistente" 
            se não existir item com chave correspondente
            ["SUCCESS"] caso tenha sido uma operação bem sucedida
        """
        self.try_read_from_file()

        # verifica se existe entrada correspondente
        inventry_entry = inInventoryDatabase.get_inventory_entry_by_ID(id_item) 
        if inventry_entry == None:
            return (False, ["Chave inexistente"])
        
        # sucesso
        self.db[inventory_entry.id_item].qnt = qnt
        self.write_to_file()
        return (True, ["SUCCESS"])

    def remove_inventory_entry_by_ID (self, id_item: str) -> InventoryEntry | None:
        """ Remover um InventoryEntry da base

        Args:
            id_item (str): ID do item em questão (unicamente identificável)

        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            reason (list[str]): contém "NOT_FOUND" se o item não foi encontrado
            ["SUCCESS"] caso tenha sido uma operação bem sucedida
        """

        self.try_read_from_file()
        toreturn = self.db.pop(id_item, None)
        self.write_to_file()
        return toreturn

    @staticmethod
    def get_inventory_entry_by_ID (self, id_item: str) -> InventoryEntry | None:
        """ Acessar um InventoryEntry da database

        Args:
            id_item (int): ID do item em questão

        Returns:
            (inventory_entry | None): InventoryEntry se existe, None se não
        """
        self.try_read_from_file()
        for key,val in self.db.items():
            if val.id_item == id_item: # val é do tipo InventoryEntry, possui atributo id_item
                return val
        return None


    def clear_database(self):
        self.db = dict()
        self.write_to_file()
        
