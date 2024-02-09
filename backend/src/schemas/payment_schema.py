from pydantic import BaseModel
import datetime

class Boleto(BaseModel): 
    type: str
    nome_completo: str
    cpf: str

class Pix(BaseModel): 
    type: str
    nome_completo: str
    cpf: str

class Cartao(Boleto):
    cvv: str
    nome_cartao: str
    num_cartao: str
    validade: datetime.date


