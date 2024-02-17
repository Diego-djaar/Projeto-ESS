from pydantic import BaseModel
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

    name: str
    _type: str 
    stock: int 
    price: float
    supplier_corporate_name: str
    supplier_name: str

class Order(BaseModel):

    supplier_name: str
    quantity: int = 1
    price: float
    request_date: datetime.date
    delivery_date: datetime.date
    delivery_model: str
    status: str
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
    orders_list: Optional[List[Order]] = None