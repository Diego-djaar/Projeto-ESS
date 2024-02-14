from pydantic import BaseModel
import datetime

class Cartao(BaseModel): 
    nome_cartao: str 
    numero_cartao: str 
    cvv: str 
    cpf: str 
    validade: datetime.date

class Pix(BaseModel):
    nome_completo: str 
    cpf: str 

class Boleto(Pix):
    pass




