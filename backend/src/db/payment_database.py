from typing import List, Dict
from uuid import uuid4
from pymongo import MongoClient, errors
from pymongo.collection import Collection, IndexModel
#from src.config.config import env
from logging import INFO, WARNING, getLogger
import datetime
import hmac
import hashlib
import re
import json 

logger = getLogger('uvicorn')

cpf_pattern = re.compile(r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$")
cartao_pattern = re.compile(r"^5[1-5][0-9]{14}$")

database = {} 

def escrever_arquivo(database): 
    with open("payment_database.json", "w") as f: 
        json.dump(database, f, default=str, indent=4)

def ler_arquivo(database): 
    with open("payment_database.json", "r") as f:
        return json.load(f)

def Adicionar_cartao(nome_cartao: str, numero_cartao: str, cvv: str, cpf: str, validade: datetime.date) -> bool: 
    #if not cpf_pattern.match(cpf):
        #raise ValueError("CPF inválido")

    #if not cartao_pattern.match(numero_cartao):
        #raise ValueError("Número de cartão inválido")

    if cpf not in database:
        database[cpf] = []

    cartao = {
        "nome_cartao": nome_cartao,
        "numero_cartao": numero_cartao,
        "cvv": cvv,
        "validade": validade.strftime("%Y-%m-%d"),
        "cpf": cpf
    }

    database[cpf].append(cartao)
    escrever_arquivo(database)

    return True 
