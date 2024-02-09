from pydantic import BaseModel
import datetime

class Boleto_pix(BaseModel): 
    type: str
    nome_completo: str
    cpf: str

class Cartao(Boleto_pix):
    cvv: str
    nome_cartao: str
    num_cartao: str
    validade: datetime.date


