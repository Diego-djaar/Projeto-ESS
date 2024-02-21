from .database import Database
from .user_database import UserDatabase
from .codigos_rec_database import RecuperacaoDatabase
from .config.create_collections import create_collections

database = Database()
user_database = UserDatabase()
user_database_example = UserDatabase("Usuários teste.json")
user_database_example.clear_database()


#create_collections(database)

from .itens_database import ItemDatabase
from .carrinho_database import Carrinhos
from .inventory_database import InventoryDatabase

item_database = ItemDatabase()
cart_database = Carrinhos()
inventory_database = InventoryDatabase()

recuperacao_database = RecuperacaoDatabase()
recuperacao_database_test = RecuperacaoDatabase("Códigos teste.json")
# create_collections(database)

