from pydantic import BaseModel
from typing import List, Optional
import datetime

# All these schemas are focus on other features, but I created them before get the schemas of others group members to test calculate the estimative of products arrival and cancel orders

class Supplier(BaseModel):

    name: str
    corporate_name: str
    CNPJ: str
    CEP: str 
    email: str
    sector: str

class Product(BaseModel):

    _id: int
    name: str
    supplier_corporate_name: str
    supplier_name: str
    CEP: str
    _type: str 
    img: str | None
    stock: int 
    price: float

class Order(BaseModel):

    _id: int
    name: str
    supplier_name: str
    _type: str 
    img: str | None
    quantity: int = 1
    price: float
    request_date: datetime.date
    delivery_date: datetime.date
    delivery_model: str
    _status: str
    cancel_reason: str | None
    payment_method: str

class User(BaseModel):

    username: str
    name: str
    last_name: str
    cpf: str
    date_of_birth: datetime.date
    email: str
    address: str | None = None
    CEP: str | None = None