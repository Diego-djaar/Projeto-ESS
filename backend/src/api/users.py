from fastapi import APIRouter, status, Response
from src.schemas.response import HttpResponseModel
from src.service.impl.signup_service import DadosCadastrais, SingUpService

router = APIRouter()

@router.post(
    "/{item_id}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Cadastro de Usuário",
    responses = {
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Usuário Cadastrado",
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": HttpResponseModel,
            "description": "Falha no Cadastro de Usuário",
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Bad Request",
        }
    },
)
def cadastrar_usuário(dados: DadosCadastrais, response: Response) -> HttpResponseModel:
    signup_get_response = SingUpService.signup_user(dados)
    response.status_code = signup_get_response.status_code
    return signup_get_response