from fastapi import APIRouter, HTTPException
from src.schemas.historico import Order, OrderFilter, getDB, validate_orders

router = APIRouter()

@router.get("/orders_by_user/{user_cpf}", status_code= 200, tags=["orders"], response_model= list[Order])
async def orders_user(user_cpf: str):
    db = getDB()
    if user_cpf in db:
        orders = db[user_cpf]
        return orders
    else:
        return []
    
@router.get("/order_from_user/{user_cpf}&{order_id}", status_code= 200, tags=["orders"], response_model= dict)
async def orders_user(user_cpf: str, order_id: int):
    db = getDB()
    if user_cpf in db:
        for order in db[user_cpf]:
            if order["id"] == order_id:
                return order
        return {}
    else:
        return {}
    
@router.post("/orders_filtered/", status_code= 200, tags=["orders"], response_model= list[Order])
async def orders_filtered(filtro: OrderFilter):
    db = getDB()
    result = []
    if filtro.cpf in db:
        orders = db[filtro.cpf]
        for order in orders:
            valid = validate_orders(filtro, order)
            if valid:
                result.append(order)
    return result