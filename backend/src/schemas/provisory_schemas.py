from pydantic import BaseModel
from typing import List, Optional
import datetime

# All these schemas are focus on other features, but I created them before get the schemas of others group members 

class Supplier(BaseModel):

    name: str
    corporate_name: str
    CNPJ: str
    CEP: str 
    email: str
    sector: str

class Product(BaseModel):

    id: int
    name: str
    supplier_corporate_name: str
    supplier_name: str
    CEP: str
    _type: str 
    img: str | None
    stock: int 
    price: float

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

class User(BaseModel):

    username: str
    name: str
    last_name: str
    cpf: str
    date_of_birth: datetime.date
    email: str
    address: str | None = None
    CEP: str | None = None