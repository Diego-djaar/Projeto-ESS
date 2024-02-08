from pydantic import typing, BaseModel
import datetime

class Pix(BaseModel):
    nome_completo: str
    cpf: str 

class Boleto(BaseModel):
    nome_completo: str
    cpf: str 

class Cartao(BaseModel): 
    nome_completo: str 
    nome_cartao: str 
    numero_cartao: str 
    cvv: str 
    validade: datetime.date



