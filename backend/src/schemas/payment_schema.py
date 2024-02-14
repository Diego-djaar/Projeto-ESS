from pydantic import BaseModel
import datetime

class cartao(BaseModel): 
    cpf: str 
    nome_cartao: str 
    numero_cartao: str 
    cvv: str 
    validade: datetime.date





