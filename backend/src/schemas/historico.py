from pydantic import BaseModel
from typing import List, Optional
import datetime
import json

def getDB():
    with open(".\src\db\pedidos.json", "r") as dbj:
        db = json.load(dbj)
    return db

class Order(BaseModel):
    id: int
    supplier_name: str
    name: str
    img: str | None
    quantity: int = 1
    price: float
    request_date: datetime.date
    delivery_date: datetime.date
    delivery_model: str
    _status: str
    payment_method: str
    composition: Optional[List['Order']] = None

class OrderFilter(BaseModel):
    cpf: str
    id: Optional[int]
    supplier_name: Optional[str]
    name: Optional[str]
    quantity: Optional[int]
    price_min: Optional[float]
    price_max: Optional[float]
    start_date: Optional[datetime.date]
    end_date: Optional[datetime.date]

def validate_orders(filter: OrderFilter, order: Order):
    valid = True
    order = Order(**order)
    if filter.id and order.id != filter.id:
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