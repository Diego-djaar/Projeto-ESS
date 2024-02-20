from typing import List, Dict
from uuid import uuid4
from pymongo import MongoClient, errors
from pymongo.collection import Collection, IndexModel
#from src.config.config import env
from logging import INFO, WARNING, getLogger
from decimal import Decimal
import re
import os.path
import jsonpickle
from pydantic import BaseModel

class DadosLojaItem(BaseModel):
    id_loja: str # id de 6 dígitos
    id_item: str # id de 8 dígitos

logger = getLogger('uvicorn')

class LojaItem():
    """Classe que associa uma loja com um item
    
        Criar com método new_item()

    Returns:
        (Item, "SUCCESS"), ou (None, reason) caso o input não seja validado.
        
        reason será o nome do campo rejeitado pela validação
    """
    id_loja: str # id de 6 dígitos
    id_item: str # id de 8 dígitos
    ID_LOJA_LENGTH = 6
    ID_ITEM_LENGTH = 8

    def __init__(self, id_loja: str, id_item: str):
        self.id_loja = id_loja
        self.id_item = id_item
    
    def to_dados_lojaitem(self):
        return DadosLojaItem(
            id_loja=self.id_loja,
            id_item=self.id_item,
        )
    
    @staticmethod
    def new_lojaitem(id_loja: str, id_item: str):
        """Cria novo mapeamento loja-item a menos que excessão seja levantada

        Args:
            id_loja : str
            id_item : str

        Returns:
            (LojaItem, "SUCESS"), ou (None, reason) caso o input não seja validado.
            
            reason será a lista dos campos rejeitados pela validação. ["SUCCESS"] caso seja validado.
        """

        reason = []
        
        # Verifica se ID item tem 8 dígitos
        if str(id_item).__len__() != LojaItem.ID_ITEM_LENGTH:
            reason.append("ID item com tamanho inválido")

        # Verifica se ID loja tem 6 dígitos
        if str(id_loja).__len__() != LojaItem.ID_LOJA_LENGTH:
            reason.append("ID loja com tamanho inválido")

        obj = None
        if reason.__len__() == 0:
            reason.append("SUCCESS")
            obj = LojaItem(id_loja, id_item)

        return (obj, reason)

class LojaItemDatabase():
    db: dict[LojaItem]
    file_path:str

    def __init__(self, path: str = "Lojaitens.json"):
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
    
    def get_lojaitens_list(self):
        """Retorna todas as entradas loja-item da base"""
        self.try_read_from_file()
        return list(self.db.values())
    
    def add_new_lojaitem(self, lojaitem: LojaItem):
        """Adicionar um novo objeto loja-item a base

        Args:
            lojaitem (Lojaitem): LojaItem em questão
            
        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            reason (list[str]): contém "LojaItem com mesmo ID já na base de dados" se for um item já existente.
            ["SUCCESS"] caso tenha sido uma operação bem sucedida
        """
        reason = []
        self.try_read_from_file()
        # verifica id do item, porque id da loja pode ocorrer mais de uma vez
        if LojaItemDatabase.get_lojaitem_by_ID(lojaitem.id_item): #---------------------------------------------------------
            reason.append("LojaItem com mesmo ID já na base de dados")
        
        if reason.__len__() > 0:
            return (False, reason)
        
        self.db[lojaitem.id_item] = lojaitem
        self.write_to_file()
        return (True, ["SUCCESS"])

    def remove_lojaitem_by_ID (self, id_item: str) -> LojaItem | None:
        """ Remover um loja-item da base

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
    def get_lojaitem_by_ID (self, id_item: str) -> LojaItem | None:
        """ Acessar um loja-item da database

        Args:
            id_item (int): ID do item em questão

        Returns:
            lojaitem (LojaItem | None): LojaItem se existe, None se não
        """
        self.try_read_from_file()
        for key,val in self.db.items():
            if val.id_item == id_item: # val é do tipo LojaItem, possui atributo id_item
                return val
        return None


    def clear_database(self):
        self.db = dict()
        self.write_to_file()
        