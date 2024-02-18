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
from src.db.itens_database import Item

logger = getLogger('uvicorn')

class Carrinho():
    """Classe que representa um carrinho de um usuário
    
        Criar com método new_cart()

    Returns:
        (Cart, "SUCCESS"), ou (None, reason) caso o input não seja validado.
        
        reason será o nome do campo rejeitado pela validação
    """
    CPF: str
    items: dict[Item]

    def __init__(self, CPF: str):
        self.CPF = CPF
        self.items = dict()
    
    def get_all_items(self):
        """Retorna todos os itens do carrinho"""
        return list(self.items.values())
    
    def add_item(self, item: Item):
        """Adicionar um item ao carrinho

        Args:
            item (Item): Item em questão
            
        Returns:
            reason (list[str]): contém informações sobre se o item já existia ou não.
        """
        reason = []
        obj = self.get_item_by_ID(item.id)
    
        if obj is None:
            self.items[item.id] = item
            reason.append("Novo item adicionado")
        else:
            self.items[item.id].quantidade += item.quantidade
            reason.append("Quantidade do item existente aumentada")

        return reason

    def remove_item_by_ID (self, item_id: int) -> Item | None:
        """ Remover um item do carrinho

        Args:
            item_id (int): ID do item em questão

        Returns:
            item (Item | None): retorna item removido ou nada
        """
        toreturn = self.items.pop(item_id, None)
        return toreturn

    def get_item_by_ID (self, item_id: int) -> Item | None:
        """ Acessar um item do carrinho

        Args:
            item_id (int): ID do item em questão

        Returns:
            Item (Item): Se o item for encontrado | None: Se o item não for encontrado.
        """
        for key,val in self.items.items():
            if val.id == item_id:
                return val
        return None
    
    def modify_item_by_ID (self, item_id: int, new_item: Item):
        """ Modificar um item da database

        Args:
            item_id (int): ID do item em questão
            new_item (Item): novos valores do item a ser modificado

        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            Item (Item | None): Se o item for encontrado.
        """
        reason = [] 
        if self.get_item_by_ID(item_id):
            reason.append("Item não encontrado")
            return(False, reason)
        
        self.items[item_id] = new_item
        return (True, ["SUCCESS"])


    def clear_database(self):
        self.items = dict()
        

class Carrinhos():
    db: dict[Carrinho]
    file_path:str

    def __init__(self, path: str = "Carrinhos.json"):
        self.db = dict()
        self.file_path = path
        self.try_read_from_file()

    def try_read_from_file(self):
        # Ler itens do arquivo
        if not os.path.exists(self.file_path):
            self.write_to_file()
            return None

        with open(self.file_path) as file:
            carrinhos = file.read()
            db = jsonpickle.decode(carrinhos)
            if type(db) == dict:
                self.db = db
    
    def write_to_file(self):
        objetos = jsonpickle.encode(self.db)
        with open(self.file_path, 'w+') as file:
            file.write(objetos)
    
    def get_cart_list(self, update = True):
        """Retorna todos os carrinhos da database"""
        if update:
            self.try_read_from_file()
        return list(self.db.values())
    
    def add_new_cart(self, carrinho: Carrinho, update: bool = True):
        """Adicionar um novo carrinho a database

        Args:
            carrinho (Carrinho): Carrinho em questão
            
        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            reason (list[str]): contém "Carrinho com mesmo CPF já na base de dados" se for um CPF já existente.
            ["SUCCESS"] caso tenha sido uma operação bem sucedida
        """
        reason = []
        if update:
            self.try_read_from_file()
        if self.get_cart_by_CPF(carrinho.CPF, False):
            reason.append("Carrinho com mesmo CPF já na base de dados")
        
        if reason.__len__() > 0:
            return (False, reason)
        
        self.db[carrinho.CPF] = carrinho
        self.write_to_file()
        return (True, ["SUCCESS"])

    def remove_cart_by_CPF (self, CPF: str, update: bool = True) -> Item | None:
        """ Remover um carrinho da database

        Args:
            CPF (str): CPF do carrinho em questão

        Returns:
            carrinho (Carrinho | None): carrinho removido ou None.
        """
        if update:
            self.try_read_from_file()
        toreturn = self.db.pop(CPF, None)
        self.write_to_file()
        return toreturn

    def get_cart_by_CPF (self, CPF: str, update: bool = True) -> Item | None:
        """ Acessar um item da database

        Args:
            CPF (str): CPF do carrinho em questão

        Returns:
            Carrinho (Carrinho | None): Carrinho se for encontrado, None se não for encontrado
        """
        if update:
            self.try_read_from_file()
        for key,val in self.db.items():
            if val.CPF == CPF:
                return val
        return None
    
    def modify_item_all_carts (self, item_id: int, new_item: Item, update: bool = True):
        """ Modificação em um item da database (chamar para aplicar alteração em todos os carrinhos que apresentam o item)

        Args:
            item_id (int): ID do item em questão
            new_item (Item): novos valores do item a ser modificado

        Returns:
            
        """
        if update:
            self.try_read_from_file()
        
        for CPF, cart in self.db:
            for id, item in cart:
                if id == item_id:
                    cart[id] = new_item

        self.write_to_file()


    def remove_item_all_carts(self, item_id: int, update: bool = True):
        """Remove um item especificado por item_id de todos os carrinhos na base de dados (chamar para aplicar alteração em todos os carrinhos que apresentam o item).

        Args:
            item_id (int): ID do item a ser removido.
            update (bool): Se True, atualiza a base de dados a partir do arquivo JSON antes da operação.

        """
        if update:
            self.try_read_from_file()

        for cart_CPF, cart in self.db.items():
            if item_id in cart.items:
                del cart.items[item_id]

        self.write_to_file()

    def add_item_to_cart(self, item: Item, CPF: str, update: bool = True):
        """Adiciona um item no carrinho

        Args:
            item (Item): item a ser adicionado
            CPF (str): CPF do carrinho a ser modificado
            update: ler do arquivo antes de operar
        
        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            reason (list[str]): contém "Carrinho não encontrado" se for o CPF não existe na base de dados.
            ["SUCCESS"] caso tenha sido uma operação bem sucedida
        """
        if update:
            self.try_read_from_file()
        
        reason = []
        carrinho = self.get_cart_by_CPF(CPF)

        if carrinho is None:
            reason.append("Carrinho de usuário não encontrado na base de dados")
            return (False, reason)

        reason = self.db[CPF].add_item(item)
        self.write_to_file()

        return (True, reason)
    
    def remove_item_from_cart(self, item_id: int, CPF: str, update: bool = True):
        """Remove um item do carrinho

        Args:
            item (Item): item a ser removido
            CPF (str): CPF do carrinho a ser modificado
            update: ler do arquivo antes de operar
        
        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            reason (list[str]): contém "Carrinho não encontrado" se for o CPF não existe na base de dados.
            contém "Item não encontrado no carrinho" se não se encontrou o item selecionado.
            ["SUCCESS"] caso tenha sido uma operação bem sucedida
        """
        if update:
            self.try_read_from_file()
        
        reason = []
        carrinho = self.get_cart_by_CPF(CPF)

        if carrinho is None:
            reason.append("Carrinho de usuário não encontrado na base de dados")
            return (False, reason)

        removed_item = self.db[CPF].remove_item_by_ID(item_id)

        if removed_item is None:
            reason.append("Item não encontrado no carrinho")
            return (False, reason)
        
        self.write_to_file()
        reason.append("SUCCESS")

        return (True, reason)
    
    def decrease_item_quantity(self, item_id: int, CPF: str, update: bool = True):
        """ Diminui em um a quantidade de um item, se o item tiver só 1 na quantidade, remove o item """
        if update:
            self.try_read_from_file()

        reason = []
        carrinho = self.get_cart_by_CPF(CPF)

        if carrinho is None:
            reason.append("Carrinho de usuário não encontrado na base de dados")
            return (False, reason)
        
        if item_id not in carrinho.items:
            reason.append("Item não encontrado no carrinho")
            return (False, reason)
        
        if carrinho.items[item_id].quantidade > 1:
            carrinho.items[item_id].quantidade -= 1
        else:
            del carrinho.items[item_id]
        
        self.write_to_file()
        reason.append("SUCCESS")

        return (True, reason)
    
    def increase_item_quantity(self, item_id: int, CPF: str, update: bool = True):
        """Aumenta a quantidade de um item no carrinho.

        Args:
            item_id (int): ID do item a ter sua quantidade aumentada.
            CPF (str): CPF do usuário associado ao carrinho.
            update (bool): Se True, atualiza a base de dados a partir do arquivo JSON.

        Returns:
            (bool, list): Tupla contendo o sucesso da operação e uma lista de razões.
        """
        if update:
            self.try_read_from_file()

        reason = []
        carrinho = self.get_cart_by_CPF(CPF)

        if carrinho is None:
            reason.append("Carrinho de usuário não encontrado na base de dados")
            return (False, reason)

        if item_id not in carrinho.items:
            reason.append("Item não encontrado no carrinho")
            return (False, reason)

        carrinho.items[item_id].quantidade += 1

        self.write_to_file()
        reason.append("SUCCESS")

        return (True, reason)
    
    def clear_cart_database(self):
        self.db = dict()
        self.write_to_file()
