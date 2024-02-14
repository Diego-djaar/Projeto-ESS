from pydantic import BaseModel
import datetime

class Cartao(BaseModel): 
    user_name: str
    nome_cartao: str 
    numero_cartao: str 
    cvv: str 
    cpf: str 
    validade: datetime.date

class Pix(BaseModel):
    user_name: str
    nome_completo: str 
    cpf: str 

class Boleto(BaseModel):
    user_name: str
    nome_completo: str 
    cpf: str 




