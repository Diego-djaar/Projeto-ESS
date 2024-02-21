from pydantic import BaseModel
from src.schemas.provisory_schemas import Order
from typing import Optional
import datetime

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
