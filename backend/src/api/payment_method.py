from fastapi import APIRouter, status, Response
from src.schemas.response import HttpResponseModel
from src.schemas.payment_method_schemas import Pix, Boleto, Cartao

router = APIRouter()

@router.post(
    "/register_payment_method/pix",
    response_model=HttpResponseModel,
    status_code=status.HTTP_201_CREATED,
    description="Payment_method insertion",
    responses={
        status.HTTP_201_CREATED: {
            "model": HttpResponseModel,
            "description": "payment method inserted",
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": HttpResponseModel,
            "description": "Fail in payment method insertion",
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Bad Request",
        },
    },
)
def payment_method_insertion(pix: Pix, response: Response) -> HttpResponseModel:
    pass
