from fastapi import APIRouter, status, HTTPException, Response
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.provisory_schemas import Supplier, Product, PreOrder, Order, User
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get(
    '/calculate_estimated_time/{product_id}/{user_CPF}',
    response_model=HttpResponseModel,
    status_code=status.HTTP_201_CREATED,
    description="Tempo estimado do produto obtido com sucesso",
    )
def get_time(product_id: Product.id, user_CPF: User.cpf) -> HttpResponseModel:
    response = TimeArrivalService.calculating_time_arrival(product_id, user_CPF)
    return response