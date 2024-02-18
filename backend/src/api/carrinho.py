from fastapi import APIRouter, status, HTTPException
from src.schemas.response import HttpResponseModel
from src.service.impl.carrinho_service import Carrinho_service
from src.service.impl.item_database_service import DadosItem

router = APIRouter()

@router.get(
    "/view",
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
    """ Se carrinho não for encontrado cria carrinho para o respectivo CPF """
    return Carrinho_service.get_cart(CPF=CPF)

@router.post(
    "/adicionar",
    response_model=HttpResponseModel,
    status_code=status.HTTP_201_CREATED,
    description="Adicionar item ao carrinho",
    responses={
        status.HTTP_201_CREATED: {
            "model": HttpResponseModel,
            "description": "Item adicionado ao carrinho com sucesso"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha na adição do item ao carrinho"
        }
    },
)
def adicionar_item_ao_carrinho(dados: DadosItem, CPF: str) -> HttpResponseModel:
    """ Tenta adicionar item ao carrinho """
    resultado = Carrinho_service.add_item_to_cart(item_data= dados, CPF= CPF)
    if resultado.status_code == status.HTTP_201_CREATED:
        return resultado
    else:
        # Se a adição não foi bem-sucedida, lançar uma exceção HTTP que será tratada pelo FastAPI
        raise HTTPException(
            status_code=resultado.status_code,
            detail=resultado.message
        )