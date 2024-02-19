from .database import Database
from .user_database import UserDatabase
from .config.create_collections import create_collections

user_database = UserDatabase()
user_database_example = UserDatabase("Usuários teste.json")
user_database_example.clear_database()
