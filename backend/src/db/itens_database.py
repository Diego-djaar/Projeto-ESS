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

class DadosItem(BaseModel):
    id: str # Acessos a database serão pelo ID (8 dígitos)
    nome: str # Nome visível na interface
    description: str
    price: str
    quantidade: int
    img: str | None # Path para o arquivo

logger = getLogger('uvicorn')

class Item():
    """Classe que representa um item da database
    
        Criar com método new_item()

    Returns:
        (Item, "SUCCESS"), ou (None, reason) caso o input não seja validado.
        
        reason será o nome do campo rejeitado pela validação
    """
    id: str # Acessos a database serão pelo ID (8 dígitos)
    nome: str # Nome visível na interface
    description: str
    price: str
    quantidade: int
    img: str | None # Path para o arquivo
    ID_LENGTH = 8

    def __init__(self, id: str, nome: str, description: str, price: str, quantidade: int, img: str | None = None):
        self.id = id
        self.nome = nome
        self.description = description
        self.price = price
        self.quantidade = quantidade
        self.img = img
    
    def to_dados_item(self):
        return DadosItem(
            id=self.id,
            nome=self.nome,
            description=self.description,
            price=self.price,
            quantidade=self.quantidade,
            img=self.img
        )


    @staticmethod
    def is_image_path(path):
        # Função para verificar se o path é válido para evitar SQL injection
        # Ela considera extensões comuns de imagem e é case-insensitive (flag re.IGNORECASE)
        pattern = re.compile(r"^[^.\n]+\.(jpg|jpeg|png|gif|bmp|tiff)$", re.IGNORECASE)
        return re.match(pattern, path) is not None
    
    @staticmethod
    def is_valid_price(price):
        # Função para verificar se o preço do produto é válido
        # Ela considera números no formato X.Y com X de no máximo 5 digitos e Y exatamente 2
        pattern = re.compile(r"^\d{1,5}\.\d{2}$", re.IGNORECASE)
        return re.match(pattern, str(price)) is not None
    
    @staticmethod
    def new_item(id: str, nome: str, description: str, price: str, quantidade: int, img: str | None = None):
        """Cria novo item, validando-o de acordo com validade do path e tamanho do ID

        Args:
            id: str
            nome: str
            description: str
            price: str -> Conversão em decimal feita na hora de fazer cálculos
            quantidade: int
            img: str | None -> Path do arquivo

        Returns:
            (Item, "SUCESS"), ou (None, reason) caso o input não seja validado.
            
            reason será a lista dos campos rejeitados pela validação. ["SUCCESS"] se o user for validado.
        """

        reason = []
        print("Entrou em new_item")
        print(id)
        # Verifica se imagem tem um formato sustentado
        if img is not None and not Item.is_image_path(img):
            reason.append("Caminho da imagem mal formulado")

        # Verifica se ID tem 8 dígitos
        if str(id).__len__() != Item.ID_LENGTH:
            reason.append("ID com tamanho inválido")

        if not Item.is_valid_price(price):
            reason.append("Preço com formato inválido")

        obj = None
        if reason.__len__() == 0:
            reason.append("SUCCESS")
            obj = Item(id, nome, description, price, quantidade, img)

        return (obj, reason)

class ItemDatabase():
    db: dict[Item]
    file_path:str

    def __init__(self, path: str = "Itens.json"):
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
    
    def get_itens_list(self, update = True):
        """Retorna todos os itens da database"""
        if update:
            self.try_read_from_file()
        return list(self.db.values())
    
    def add_new_item(self, item: Item, update: bool = True):
        """Adicionar um novo item a database

        Args:
            item (Item): Item em questão
            
        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            reason (list[str]): contém "Item com mesmo ID já na base de dados" se for um item já existente.
            ["SUCCESS"] caso tenha sido uma operação bem sucedida
        """
        reason = []
        if update:
            self.try_read_from_file()
        if ItemDatabase.get_item_by_ID(item.id, False):
            reason.append("Item com mesmo ID já na base de dados")
        
        if reason.__len__() > 0:
            return (False, reason)
        
        self.db[item.id] = item
        self.write_to_file()
        return (True, ["SUCCESS"])

    def remove_item_by_ID (self, item_id: str, update: bool = True) -> Item | None:
        """ Remover um item da database

        Args:
            item_id (int): ID do item em questão

        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            reason (list[str]): contém "NOT_FOUND" se o item não foi encontrado
            ["SUCCESS"] caso tenha sido uma operação bem sucedida
        """
        if update:
            self.try_read_from_file()
        toreturn = self.db.pop(item_id, None)
        self.write_to_file()
        return toreturn

    @staticmethod
    def get_item_by_ID (self, item_id: str, update: bool = True) -> Item | None:
        """ Acessar um item da database

        Args:
            item_id (int): ID do item em questão

        Returns:
            item (Item | None): Item se existe, None se não
        """
        if update:
            self.try_read_from_file()
        for key,val in self.db.items():
            if val.id == item_id:
                return val
        return None
    
    def modify_item_by_ID (self, item_id: str, new_item: Item, update: bool = True):
        """ Modificar um item da database

        Args:
            item_id (int): ID do item em questão
            new_item (Item): novos valores do item a ser modificado

        Returns:
            success (bool): True para operação bem sucedida, False para mal sucedida
            Item (Item | None): Se o item for encontrado.
        """
        reason = []
        if update:
            self.try_read_from_file()
        
        if ItemDatabase.get_item_by_ID(item_id, False):
            reason.append("Item não encontrado")
            return(False, reason)
        
        self.db[item_id] = new_item
        self.write_to_file()
        return (True, ["SUCCESS"])


    def clear_database(self):
        self.db = dict()
        self.write_to_file()
        