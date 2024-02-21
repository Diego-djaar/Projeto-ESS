from .user_database import UserDatabase
from .codigos_rec_database import RecuperacaoDatabase
from .store_database import StoreDatabase
user_database = UserDatabase()
user_database_example = UserDatabase("Usuários teste.json")
user_database_example.clear_database()


from .itens_database import ItemDatabase
from .carrinho_database import Carrinhos

item_database = ItemDatabase()

cart_database = Carrinhos()
store_database = StoreDatabase()
recuperacao_database = RecuperacaoDatabase()
recuperacao_database_test = RecuperacaoDatabase("Códigos teste.json")

