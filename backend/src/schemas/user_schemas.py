from pydantic import BaseModel
from src.db.user_database import User
import datetime

class Token(BaseModel):
    token: str

class DadosLogin(BaseModel):
    cpf_ou_user_ou_email: str
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
    
    def from_user(user: User):
        return DadosUser(
            username=user.username,
            nome=user.nome,
            sobrenome=user.sobrenome,
            cpf=user.cpf,
            data_de_nascimento=user.data_de_nascimento,
            email=user.email,
            CEP=user.CEP,
            endereço=user.endereço
        )
        
    
    
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
    