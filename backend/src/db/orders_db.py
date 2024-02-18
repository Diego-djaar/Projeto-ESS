from typing import List, Dict
from logging import INFO, WARNING, getLogger
from datetime import datetime, timedelta
import json
import os

logger = getLogger('uvicorn')

database_orders = {}

def read_file(database, file):
    file_path = os.path.join(os.path.dirname(__file__), file) 
    with open(file_path, "r") as f:
        return json.load(f)

def write_file(database, file):
    file_path = os.path.join(os.path.dirname(__file__), file)
    with open(file_path, "w") as f:
        json.dump(database, f, indent=4)

def cancel_order_db(product_id:int, user_CPF: str,cancel_reason:str) -> (bool, {}):

    orders_db = read_file(database_orders, "orders.json")

    if (cancel_reason == ""):
        return (False,{"No cancel reason": True})
    if user_CPF not in orders_db:
        return (False, {"CPF not found": True})
    

    for order in orders_db[user_CPF]:
        if order["id"] == product_id:
            if order["_status"] == "Canceled":
                return (False, {'canceled': True})
            elif order["_status"] == "Delivered":
                return (False, {'delivered': True})
            elif order["_status"] == "On the way":
                order["_status"] = "Canceled"
                order["cancel_reason"] = cancel_reason

                write_file(orders_db, "orders.json")

                return(True, {})

    return (False, {"ID not found": True})

def get_all_orders_db(user_CPF: str) -> (bool, []):

    orders_db = read_file(database_orders, "orders.json")

    canceled_orders = []

    for order in orders_db[user_CPF]:
        if order["_status"] == "Canceled":
            canceled_orders.append(order)
    
    if len(canceled_orders) == 0:
        return (False, [])
    else:
        return (True, canceled_orders)