from fastapi import APIRouter, status, HTTPException
from src.service.impl.payment_method_service import PaymentService
from src.schemas.payment_schema import Cartao, Boleto, Pix
from src.schemas.response import HTTPResponses, HttpResponseModel
from fastapi.responses import JSONResponse


router = APIRouter()

@router.post(
        '/inserting/cartao', 
        response_model=HttpResponseModel,
        summary="Create a new payment method", 
             )
def insert_payment(cartao: Cartao) -> HttpResponseModel: 
    response = PaymentService.inserting_cartao(cartao)
    return response 

@router.post(
        '/inserting/pix', 
        response_model=HttpResponseModel,
        summary="Create a new payment method", 
             )
def insert_payment(pix: Pix) -> HttpResponseModel: 
    response = PaymentService.insertion_pix(pix)
    return response 

@router.post(
        '/inserting/boleto', 
        response_model=HttpResponseModel,
        summary="Create a new payment method", 
             )
def insert_payment(boleto: Boleto) -> HttpResponseModel: 
    response = PaymentService.insertion_boleto(boleto)
    return response 

# @router.post(
#     "/inserting/{method_name}",
#     response_model=HttpResponseModel,
#     summary="Create a new payment method"
# )
# def insert_payment_method(method_name: str, cartao: Cartao, pix: Pix, boleto: Boleto) -> HttpResponseModel:
#     if method_name == "boleto": 
#         response = PaymentService.inserting_cartao(boleto)
#         return response 
#     elif method_name == "pix": 
#         response = PaymentService.insertion_pix(pix)
#         return response 
#     elif method_name == "cartao":
#         response = PaymentService.inserting_cartao(cartao)
#         return response 