from logging import getLogger
import json
import os
from src.schemas.history import OrderFilter
from src.schemas.provisory_schemas import Order

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

def orders_user(user_CPF: str):
    db = read_file({}, "orders.json")
    if user_CPF in db:
        orders = db[user_CPF]
        return orders
    else:
        return []

def order_user(user_CPF: str, order_id: int):
    db = read_file({}, "orders.json")
    if user_CPF in db:
        for order in db[user_CPF]:
            if order["id"] == order_id:
                return order
    return {}

def orders_filtered(filtro: OrderFilter):
    db = read_file({}, "orders.json")
    result = []
    if filtro.cpf in db:
        orders = db[filtro.cpf]
        for order in orders:
            valid = validate_orders(filtro, order)
            if valid:
                result.append(order)
    return result
    
def validate_orders(filter: OrderFilter, order_: Order):
    valid = True
    order = Order(**order_)
    if filter.id and order_['id'] != filter.id:
        valid = False
    if valid and filter.supplier_name and filter.supplier_name.lower() not in order.supplier_name.lower():
        valid = False
    if valid and filter.name and filter.name.lower() not in order.name.lower():
        valid = False
    if valid and filter.quantity and filter.quantity != order.quantity:
        valid = False
    if valid and filter.price_min and (order.price < filter.price_min):
        valid = False
    if valid and filter.price_max and (order.price > filter.price_max):
        valid = False
    if valid and filter.start_date and (order.request_date < filter.start_date):
        valid = False
    if valid and filter.end_date and (order.request_date > filter.end_date):
        valid = False
    return valid
