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

    problemas = []

    if not cpf_pattern.match(cpf):
        problemas.append("CPF")

    if not validade >= datetime.date.today():
      problemas.append("VALIDADE")

    # if not cartao_pattern.match(numero_cartao):
    #     problemas.append("CARD_NUMBER")cx

    if len(problemas) > 0:
        return (False, problemas)

    if cpf not in database:
        database[cpf] = []

    cartao = {
        "id" : abs(hash((datetime.datetime.now(), cpf))), 
        "tipo": "cartao", 
        "nome_cartao": nome_cartao,
        "numero_cartao": numero_cartao,
        "cvv": cvv,
        "validade": validade.strftime("%Y-%m-%d"),
        "cpf": cpf
    }

    database[cpf].append(cartao)
    escrever_arquivo(database)

    return (True, problemas)

def Adicionar_pix(nome_completo: str, cpf: str): 

    if cpf not in database:
        database[cpf] = []

    pix = {
        "id" : abs(hash((datetime.datetime.now(), cpf))), 
        "tipo": "pix", 
        "nome_completo": nome_completo,
        "cpf": cpf
    }

    database[cpf].append(pix)
    escrever_arquivo(database)

def Adicionar_boleto(nome_completo: str, cpf: str): 

    if cpf not in database:
        database[cpf] = []

    pix = {
        "id" : abs(hash((datetime.datetime.now(), cpf))), 
        "tipo": "boleto", 
        "nome_completo": nome_completo,
        "cpf": cpf
    }

    database[cpf].append(pix)
    escrever_arquivo(database)

def obter_lista_de_metodos_pagamento(cpf: str): 

    dados = ler_arquivo(database)

    if cpf in dados: 
        metodos_usuario = dados[cpf]
    else: 
        metodos_usuario = None
        
    return metodos_usuario

def atualizar_cartao(id: int, nome_cartao: str, numero_cartao: str, cvv: str, validade: datetime.date):

    dados = ler_arquivo(database)

    problemas = []

    for chave in dados:
        for valor in dados[chave]: 
                if valor["id"] == id:

                    if not validade >= datetime.date.today():
                        problemas.append("VALIDADE")

                    # if not cartao_pattern.match(numero_cartao):
                    #     problemas.append("CARD_NUMBER")cx

                    if len(problemas) > 0:
                        return (False, problemas)
                    
                    valor["nome_cartao"] = nome_cartao
                    valor["numero_cartao"] = numero_cartao
                    valor["cvv"] = cvv 
                    valor["validade"] = validade
                    
                    escrever_arquivo(dados)

                    return (True, ["SUCESS"])
                else:
                    problemas.append("ID_NOT_FOUND")
                    return (False, problemas)

def atualizar_boleto_pix(id: int, nome_completo: str):

        dados = ler_arquivo(database)

        for chave in dados:
            for valor in dados[chave]: 
                if valor["id"] == id:
                    valor["nome_completo"] = nome_completo
                    escrever_arquivo(dados)
                    return True
                else:
                    return False

def deletar_metodo(id: int): 

    dados = ler_arquivo(database)

    for chave in dados:
        for valor in dados[chave]: 
                if valor["id"] == id:

                    index = dados[chave].index(valor)
            
                    del dados[chave][index]

                    escrever_arquivo(dados)

                    return True 

                else: 
                    return False 






