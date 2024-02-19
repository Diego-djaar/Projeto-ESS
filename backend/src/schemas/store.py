from pydantic import BaseModel
from enum import Enum

class Categoria(Enum):
    cat1 = 'Alimenticio'
    cat2 = "Textil"


# Model for user credentials
class Store(BaseModel):
    cnpj: str
    username: str
    email: str
    categoria: Categoria
    password: str

