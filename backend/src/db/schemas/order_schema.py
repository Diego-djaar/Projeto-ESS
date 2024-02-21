from pydantic import BaseModel
import datetime
from src.db.itens_database import Item

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

def convert_cart_to_orders(cart_items: list[Item]):
    orders = []
    order_id = 1

    # Agrupando itens por fornecedor
    items_by_supplier = dict()
    for item in cart_items:
        items_by_supplier[item.supplier_name].append(item)

    # Criando pedidos
    for supplier, items in items_by_supplier.items():
        total_price = sum(item.price * item.quantity for item in items)
        total_quantity = sum(item.quantity for item in items)

        # Criar um pedido para cada fornecedor
        order = Order(
            _id=order_id,
            name=', '.join([item.name for item in items]),
            supplier_name=supplier,
            _type="Agrupado",
            img=None,  # ou alguma lógica para definir a imagem
            quantity=total_quantity,
            price=total_price,
            request_date=datetime.date.today(),
            delivery_date=datetime.date.today() + datetime.timedelta(days=7),  # Mudar para o cálculo do tempo de entrega
            delivery_model="Padrão",
            _status="Pendente",
            cancel_reason=None,
            payment_method="Cartão"  # Exemplo
        )
        orders.append(order)
        order_id += 1

    return orders