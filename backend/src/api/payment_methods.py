from fastapi import APIRouter, status, HTTPException
from src.service.impl.payment_method_service import PaymentService
from src.schemas.payment_schema import Cartao, Boleto, Pix, CartaoUpdate, PixUpdate, BoletoUpdate
from src.schemas.response import HTTPResponses, HttpResponseModel
from fastapi.responses import JSONResponse


router = APIRouter()

@router.post(
        '/inserting/cartao', 
        response_model=HttpResponseModel,
        status_code=201, 
        description="Insert a new card", 
             )
def insert_payment(cartao: Cartao) -> HttpResponseModel: 
    response = PaymentService.inserting_cartao(cartao)
    return response 

@router.post(
        '/inserting/pix', 
        response_model=HttpResponseModel,
        status_code=201, 
        description="Insert a new pix acount", 
             )
def insert_payment(pix: Pix) -> HttpResponseModel: 
    response = PaymentService.insertion_pix(pix)
    return response 

@router.post(
        '/inserting/boleto', 
        response_model=HttpResponseModel,
        status_code=201, 
         description="Insert a new boleto acount", 
             )
def insert_payment(boleto: Boleto) -> HttpResponseModel: 
    response = PaymentService.insertion_boleto(boleto)
    return response 

@router.get(
    "/get/payment_methods", 
    description="Get the payments methods of a especific user"
)
def get_payment_methods(username:str): 

    request = PaymentService.get_payment_methods(username)

    return request 

@router.put(
    "update/cartao/{card_id}", 
    response_model=HttpResponseModel, 
    status_code=200, 
    description="Update the card payment method"
)
def update_payment(card_id: int, cartao: CartaoUpdate): 
    
    response = PaymentService.update_cartao(card_id, cartao)

    return response

@router.put(
    "/update/pix/{card_id}", 
    response_model=HttpResponseModel, 
    status_code=200, 
    description="Update the pix payment method"
)
def update_payment(card_id: int, pix: PixUpdate): 
    
    response = PaymentService.update_pix(card_id, pix)

    return response

@router.put(
    "/update/boleto/{card_id}", 
    response_model=HttpResponseModel, 
    status_code=200, 
    description="Update the boleto payment method"
)
def update_payment(card_id: int, boleto: BoletoUpdate): 
    
    response = PaymentService.update_boleto(card_id, boleto)

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