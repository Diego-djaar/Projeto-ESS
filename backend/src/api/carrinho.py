from fastapi import APIRouter, status
from src.schemas.response import HttpResponseModel
from src.service.impl.carrinho_service import Carrinho_service

router = APIRouter()

@router.get(
    "/carrinho",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Visualização do carrinho",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Conteúdo do carrinho obtido com sucesso"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha na obtenção do conteúdo do carrinho"
        }
    },
)
def visualizar_carrinho(CPF: str) -> HttpResponseModel:
    return Carrinho_service.get_cart(CPF=CPF)
