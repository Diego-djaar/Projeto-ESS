from typing import List, Dict
from logging import INFO, WARNING, getLogger
from datetime import datetime, timedelta
from math import radians, sin, cos, sqrt, atan2
import json
import os
import requests

logger = getLogger('uvicorn')

database_user = {}
database_product = {}

def read_file(database, file):
    file_path = os.path.join(os.path.dirname(__file__), file) 
    with open(file_path, "r") as f:
        return json.load(f)

def validate_CEP(cep: str):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    api_response = requests.get(url).json()

    if ('cep' not in api_response) == True:
        return False
    else:
        return True

def haversine_distance(coord1, coord2):
    # Raio médio da terra 
    R = 6371000.0

    # Converte as coordenadas de graus para radianos
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    # Diferenças nas coordenadas
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distância em kilometros
    distance = (R * c)/1000

    return distance

def regions_relations(CEP1, CEP2):

    url_cep1 = f'https://viacep.com.br/ws/{CEP1}/json/'
    response_cep1 = requests.get(url_cep1)

    state1 = (response_cep1.json()['uf'])

    url_cep2 = f'https://viacep.com.br/ws/{CEP2}/json/'
    response_cep2 = requests.get(url_cep2)

    state2 = (response_cep2.json()['uf'])

    brasil = {'ne' : ['AL','BA','CE','MA','PB','PI','PE','RN','SE'],
    'no' : ['AC','AM','AP','PA','RO','RR','TO'],
    'co' : ['GO','MS','MT'],
    'se' : ['ES','MG','RJ','SP'],
    's' : ['PR','RS','SC']
    }

    same_region = False

    for key in brasil:
        if state1 in brasil[key]:
            region_state1 = key
    
    if state2 in brasil[region_state1]:
        same_region = True

    if state1 == state2:
        return 'same states'
    elif same_region:
        return 'same regions'
    else:
        return 'different regions'

def calculate_distance(product_CEP: str, user_CEP: str):
    url_product = f'https://brasilapi.com.br/api/cep/v2/{product_CEP}'
    response_product = requests.get(url_product)

    product_coordinates = (float(response_product.json()['location']['coordinates']['latitude']),float(response_product.json()['location']['coordinates']['longitude']))

    url_user = f'https://brasilapi.com.br/api/cep/v2/{user_CEP}'
    response_user = requests.get(url_user)

    user_coordinates = (float(response_user.json()['location']['coordinates']['latitude']),float(response_user.json()['location']['coordinates']['longitude']))

    distance = haversine_distance(product_coordinates,user_coordinates)
    
    return distance

def calculate_date(distance, transportation_type):
    if transportation_type == 'traditional':
        average_speed = 60
    elif transportation_type == 'express':
        average_speed = 80
    else:
        average_speed = 100
    
    begin_day = datetime.now()
    max_daily_time = 6  # h
    remaining_distance = distance  # km
    total_time = 0  # h
    days_worked = 0 
    delivery_date = 0  
    logistic_days = 4 

    while remaining_distance > 0:
        # Calculate the hours to run on day
        daily_time_hours = min(max_daily_time, remaining_distance / average_speed)

        # Update remaining distance
        remaining_distance -= daily_time_hours * average_speed

        days_worked += 1

        # Discounting rest days
        if days_worked > 6:
            delivery_date += 3
            days_worked = 0
        else:
            delivery_date += 1
            
    # Convertendo para um objeto datetime no final
    delivery_date = begin_day + timedelta(days=delivery_date) + timedelta(days=logistic_days)
    formatted_date = delivery_date.strftime("%d-%m-%Y")
    
    return formatted_date

def calculate_time_arrival_db(id: int, user_CPF: str) -> (bool,{}):
        
    # Read from the JSON with users the right cep
    users_db = read_file(database_user, "users.json")
    user_CEP = users_db[user_CPF]["CEP"]

        # Exception for the CEP invalid
    if not validate_CEP(user_CEP):
        return (False,{'error': True})
    else:
        id_str = str(id)

        # Read from the JSON  with orders the right cep
        products_db = read_file(database_product,"products.json")
        product_CEP = products_db[id_str]["cep"]

        # Check the type of transportation based on the CEP states
        if regions_relations(product_CEP, user_CEP) == 'same states':
            transportation = 'Traditional delivery'
        elif regions_relations(product_CEP, user_CEP) == 'same regions':
            transportation = 'Express delivery'
        else:
            transportation = 'Air delivery'
        distance = calculate_distance(product_CEP, user_CEP)

        delivery_date = calculate_date(distance, transportation)

        request_date = datetime.now().strftime("%d-%m-%Y")
        
        return (True, {'delivery_model': transportation, 'request_date':request_date,'delivery_date': delivery_date})