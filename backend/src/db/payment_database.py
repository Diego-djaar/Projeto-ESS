import os
from typing import List, Dict
from uuid import uuid4
import jsonpickle
from pymongo import MongoClient, errors
from pymongo.collection import Collection, IndexModel
#from src.config.config import env
from logging import INFO, WARNING, getLogger
import datetime
import hmac
import hashlib
import re
import json 
import datetime 
import uuid 


logger = getLogger('uvicorn')

#Regex for CPF and card number. 
cpf_pattern = re.compile(r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$")
cartao_pattern = re.compile(r"^(4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9]{2})[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])?[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$")
   
def write_file(database): 

    """Write the content of a dict in a JSON. 

    Input: database: dict.

    Process: Open the JSON file and overwrite it's content. 

    Output: JSON file overwrited.  """

    with open("payment_database.json", "w") as f: 
        json.dump(database, f, default=str, indent=4)

def read_file(): 
    with open("payment_database.json", "r") as f:
        return json.load(f)

database = {}
database = read_file()

def validate_CPF(cpf: str) -> bool: 

    """Validate a CPF number. 

    Input: a CPF number. 

    Process: verify the validity of a CPF number using a regex.

    Outuput: A boolean indicating the validity or not of the CPF number. """

    if not cpf_pattern.match(cpf):
        return False 
    
    return True 

def validate_date(validade: datetime.date) -> bool:

    """Validate a validity date. 

    Input: a date. 

    Process: compare the input date with the today date.

    Outuput: A boolean indicating the validity or not of the input date. """


    if not validade >= datetime.date.today():
        return False 
    
    return True 

def validate_card_number(numero_cartao: str) -> bool:

    """Validate a card number. 

    Input: a card number. 

    Process: verify the validity of the card number using a regex.

    Outuput: A boolean indicating the validity or not of the card number.  """

    if not cartao_pattern.match(numero_cartao):
        return False 
    
    return True 

def insert_card(nome_cartao: str, numero_cartao: str, cvv: str, cpf: str, validade: datetime.date): 

    """Validate and insert or not a card. 

    Input: the card information pass by the service layer. 

    Process: use the "validate_cpf", "validate_date" and "validate_card_number" for verify the validity of the card informations.
    if the informations is valid, the card is insert in a dict and writted in the JSON file. 

    Output: A tuple contain the sucess (bool) of the insertion and the problems (List) in case of validation problem. """


    problems = []

    if not validate_CPF(cpf):
        problems.append("CPF")

    if not validate_date(validade):
      problems.append("VALIDADE")

    if not validate_card_number(numero_cartao):
        problems.append("CARD_NUMBER")

    if len(problems) > 0:
        return (False, problems)

    if cpf not in database:
        database[cpf] = []

    id_value = str(abs(hash((datetime.date.today(), cpf))))

    cartao = {
        "id" : id_value, 
        "tipo": "cartao", 
        "nome_cartao": nome_cartao,
        "numero_cartao": numero_cartao,
        "cvv": cvv,
        "validade": validade.strftime("%Y-%m-%d"),
        "cpf": cpf
    }

    database[cpf].append(cartao)
    write_file(database)

    return (True, id_value)

def insert_pix(nome_completo: str, cpf: str) : 

    """Validate and insert or not a pix. 

    Input: the pix information pass by the service layer. 

    Process: use the "validate_cpf" for verify the validity of the pix informations.
    if the informations is valid, the pix is insert in a dict and writted in the JSON file. 

    Output: A tuple contain the sucess (bool) of the insertion. """

    result = validate_CPF(cpf)

    if not result: 
        return ("CPF", None)
    
    if cpf not in database:
        database[cpf] = []       

    for val in database[cpf]:
        if val["tipo"] == "pix":
            return ("ALREADY_EXIST", None)
        
    id_value = str(abs(hash((datetime.date.today(), cpf))))
    
    pix = {
        "id" : id_value, 
        "tipo": "pix", 
        "nome_completo": nome_completo,
        "cpf": cpf
    }

    database[cpf].append(pix)
    write_file(database)

    print(database)

    return ("OK", id_value) 

def insert_ticket(nome_completo: str, cpf: str) -> str:


    """Validate and insert or not a ticket. 

    Input: the ticket information pass by the service layer. 

    Process: use the "validate_cpf" for verify the validity of the ticket informations.
    if the informations is valid, the ticket is insert in a dict and writted in the JSON file. 

    Output: A tuple contain the sucess (bool) of the insertion. """

    result = validate_CPF(cpf)

    if not result: 
        return ("INVALID_CPF", None)
    
    if cpf not in database:
        database[cpf] = []

    for val in database[cpf]:
        if val["tipo"] == "boleto":
            return ("ALREADY_EXIST", None)
        
    id_value = str(abs(hash((datetime.date.today(), cpf))))

    boleto = {
        "id" : id_value, 
        "tipo": "boleto", 
        "nome_completo": nome_completo,
        "cpf": cpf
    }

    database[cpf].append(boleto)
    write_file(database)

    return ("OK", id_value)  

def update_card(id: str, nome_cartao: str, numero_cartao: str, cvv: str, validade: datetime.date):

    database = read_file()

    """Update the nome_cartao, numero_cartao, cvv and validade fields. 

    #Input: the card informations (id, nome_cartao, numero_cartao, cvv and validade).

    #Process: Verify if the card is in the database (using the ID). If the card is in database, 
    make the validation of card number and validity date. If the validation is sucessfull, 
    update the card information in the database and write in the JSON file
    
    Output: a tuple with the result and a array with the problems"""

    problems = []


    for key in database:
        for val in database[key]: 
                if val["id"] == id:

                    if not validade >= datetime.date.today():
                        problems.append("VALIDADE")

                    if not cartao_pattern.match(numero_cartao):
                        problems.append("CARD_NUMBER")

                    if len(problems) > 0:
                        return (False, problems)
                    
                    val["nome_cartao"] = nome_cartao
                    val["numero_cartao"] = numero_cartao
                    val["cvv"] = cvv 
                    val["validade"] = validade
                    
                    write_file(database)

                    print(database)

                    return (True, ["SUCESS"])
                
    problems.append("ID_NOT_FOUND")
    return (False, problems)


def update_pix_or_ticket(id: str, nome_completo: str) -> bool:
        

                
    for key in database:
        for val in database[key]: 
            if val["id"] == id:
                val["nome_completo"] = nome_completo
                write_file(database)
                return True
                
        return False

def delete_method(id: str) -> bool: 



    for key in database:
        for val in database[key]: 
                
                if val["id"] == id:

                    index = database[key].index(val)
            
                    del database[key][index]

                    if len(database[key]) == 0:
                        del database[key]

                    write_file(database)

                    return True 
 
    return False 

def get_by_number(numero_cartao: str):


    for key in database:
        for val in database[key]: 
            if val["tipo"] == "cartao": 
                if val["numero_cartao"] == numero_cartao:
                
                    return val 
                
    return None