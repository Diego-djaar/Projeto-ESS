from pydantic import BaseModel
import datetime

class DadosLogin(BaseModel):
    cpf: str
    senha: str
    
class DadosUser(BaseModel):
    username: str
    nome: str
    sobrenome: str
    cpf: str
    data_de_nascimento: datetime.date
    email: str
    endereço: str | None = None
    CEP: str | None = None
    
    
class DadosCadastrais(BaseModel):
    username: str
    nome: str
    sobrenome: str
    cpf: str
    data_de_nascimento: datetime.date
    email: str
    senha: str
    endereço: str | None = None
    CEP: str | None = None
    