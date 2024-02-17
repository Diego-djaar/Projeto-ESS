from .database import Database
from .config.create_collections import create_collections

database = Database()

#create_collections(database)

from .itens_database import ItemDatabase
from .carrinho_database import Carrinhos

item_database = ItemDatabase()

cart_database = Carrinhos()