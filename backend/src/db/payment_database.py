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

def Adicionar_cartao(user_name: str, nome_cartao: str, numero_cartao: str, cvv: str, cpf: str, validade: datetime.date) -> bool: 

    problemas = []

    if not cpf_pattern.match(cpf):
        problemas.append("CPF")

    if not validade >= datetime.date.today():
      problemas.append("VALIDADE")

    # if not cartao_pattern.match(numero_cartao):
    #     problemas.append("CARD_NUMBER")cx

    if len(problemas) > 0:
        return (False, problemas)

    if user_name not in database:
        database[user_name] = []

    cartao = {
        "nome_cartao": nome_cartao,
        "numero_cartao": numero_cartao,
        "cvv": cvv,
        "validade": validade.strftime("%Y-%m-%d"),
        "cpf": cpf
    }

    database[user_name].append(cartao)
    escrever_arquivo(database)

    return (True, problemas)

def Adicionar_pix(user_name: str, nome_completo: str, cpf: str): 

    if user_name not in database:
        database[cpf] = []

    pix = {
        "tipo": "pix", 
        "nome_completo": nome_completo,
        "cpf": cpf
    }

    database[user_name].append(pix)
    escrever_arquivo(database)

def Adicionar_boleto(user_name:str, nome_completo: str, cpf: str): 

    if user_name not in database:
        database[cpf] = []

    pix = {
        "tipo": "boleto", 
        "nome_completo": nome_completo,
        "cpf": cpf
    }

    database[user_name].append(pix)
    escrever_arquivo(database)

