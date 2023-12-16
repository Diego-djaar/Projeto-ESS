from .database import Database
from .user_database import UserDatabase
from .config.create_collections import create_collections

database = Database()
user_database = UserDatabase()
user_database_example = UserDatabase("Usuários teste.json")

# create_collections(database)