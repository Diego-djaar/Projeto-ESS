from fastapi import APIRouter, status, HTTPException, Response
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.schemas.provisory_schemas import Supplier, Product, PreOrder, Order, User


router = APIRouter()

@router.post(
    '/create_preorder',
    response_model=HttpResponseModel,
    status_code=status.HTTP_201_CREATED,
    description="Pré-ordem do produto criada!",
    responses={
        status.HTTP_201_CREATED: {
            "model": HttpResponseModel,
            "description": "Pré-ordem do produto criada!"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Bad request", 
        }
    }
)
def create_preorder(product: Product, response: Response) -> HttpResponseModel:
    pass

@router.put(
    '/update_preorder',
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Pré-ordem atualizada com sucesso!",
    responses={
        status.HTTP_201_CREATED: {
            "model": HttpResponseModel,
            "description": "Pré-ordem do produto criada!"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Bad request", 
        }
    }
)
def update_preorder(preorder_id:int, preorder: PreOrder) -> HttpResponseModel:
    pass

@router.delete(
    '/delete_preorder',
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Pré-ordem deletada com sucesso!",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Pré-ordem deletada com successo!"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Bad request", 
        }
    }
)
def delete_preorder(preorder_id: int) -> HttpResponseModel:
    pass