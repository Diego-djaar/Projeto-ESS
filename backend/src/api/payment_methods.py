from fastapi import APIRouter, status, HTTPException
from src.service.impl.payment_method_service import PaymentService
from src.schemas.payment_schema import Boleto
from src.schemas.response import HTTPResponses, HttpResponseModel
from fastapi.responses import JSONResponse


router = APIRouter()

@router.post(
        '/inserting', 
        response_model=HttpResponseModel,
        status_code=status.HTTP_200_OK, 
        description="Create a new payment method", 
             )
def insert_payment(boleto: Boleto) -> HttpResponseModel: 
    response = PaymentService.inserting_method(boleto)
    return JSONResponse(content="se loko", status_code=200)

# @router.get(
#     "/payment", 
#     response_model=HttpResponseModel,
#     status_code=status.HTTP_200_OK, 
#     description="Getting a payment method", 
# )
# def get_payment() -> HttpResponseModel: 
#     pass 