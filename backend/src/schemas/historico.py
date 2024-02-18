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

def validate_orders(filtro: OrderFilter, object: Order):
    valid = True
    object = Order(**object)
    if filtro.id and object.id != filtro.id:
        valid = False
    if valid and filtro.supplier_name and filtro.supplier_name.lower() not in object.supplier_name.lower():
        valid = False
    if valid and filtro.name and filtro.name.lower() not in object.name.lower():
        valid = False
    if valid and filtro.quantity and filtro.quantity != object.quantity:
        valid = False
    if valid and filtro.price_min and (object.price < filtro.price_min):
        valid = False
    if valid and filtro.price_max and (object.price > filtro.price_max):
        valid = False
    if valid and filtro.start_date and (object.request_date < filtro.start_date):
        valid = False
    if valid and filtro.end_date and (object.request_date > filtro.end_date):
        valid = False
    return valid