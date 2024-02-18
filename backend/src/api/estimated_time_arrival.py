from fastapi import APIRouter, status, HTTPException, Response
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.provisory_schemas import Supplier, Product, Order, User
from fastapi.responses import JSONResponse
from src.service.impl.time_arrival_service import TimeArrivalService


router = APIRouter()

@router.get(
    '/get_estimated_time/{product_id}',
    response_model=HttpResponseModel,
    status_code=status.HTTP_201_CREATED,
    description="Tempo estimado do produto obtido com sucesso",
    )
def get_time(product_id: int, user_CPF: str) -> HttpResponseModel:
    response = TimeArrivalService.calculating_time_arrival(product_id, user_CPF)
    return response