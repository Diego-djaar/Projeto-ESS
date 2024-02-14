from fastapi import APIRouter, status, HTTPException
from src.service.impl.payment_method_service import PaymentService
from src.schemas.payment_schema import Cartao, Boleto, Pix
from src.schemas.response import HTTPResponses, HttpResponseModel
from fastapi.responses import JSONResponse


router = APIRouter()

@router.post(
        '/inserting/cartao', 
        response_model=HttpResponseModel,
        status_code=status.HTTP_201_CREATED, 
        summary="Create a new payment method", 
             )
def insert_payment(cartao: Cartao) -> HttpResponseModel: 
    response = PaymentService.inserting_method(cartao)
    return response 

@router.post(
    "/inserting/{method_name}",
    summary="Inserting a new payment method"
)
def insert_payment_method(method_name: str, cartao: Cartao, pix: Pix, boleto: Boleto) -> HttpResponseModel:
    pass