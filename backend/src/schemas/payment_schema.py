from pydantic import BaseModel
import datetime

class PaymentBase(BaseModel): 
    nome_completo: str
    cpf: str

class Pix(PaymentBase):
    pass 

class Boleto(PaymentBase):
    pass

class Cartao(PaymentBase):
    cvv: str
    nome_cartao: str
    num_cartao: str
    validade: datetime.date


