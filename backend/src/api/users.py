from fastapi import APIRouter, status, Response
from src.schemas.response import HttpResponseModel
from src.service.impl.signup_service import DadosCadastrais, SingUpService
from src.service.impl.auth_service import DadosLogin, AuthService, DadosUser
import src.schemas.user_schemas as schemas
from src.service.impl.update_user_service import UpdateUserService

router = APIRouter()

@router.post(
    "/register",
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

@router.post(
    "/login",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Login de Usuário. Use o token recebido para manter a sessão"
)
def login_usuário(dados: DadosLogin, response: Response) -> HttpResponseModel:
    login_response = AuthService.login_user(dados)
    response.status_code = login_response.status_code
    return login_response

@router.post(
    "/verify",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retorna os dados de usuário referentes ao token de sessão"
)
def verify_usuário(token: schemas.Token, response: Response) -> HttpResponseModel:
    login_response = AuthService.get_user_data(token.token)
    response.status_code = login_response.status_code
    return login_response

@router.delete(
    "/remove",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Remove o usuário. É deslogado e removido do sistema"
)
def remove_usuário(token: schemas.Token, response: Response)  -> HttpResponseModel:
    user = AuthService.unlogin_user_internal(token.token)
    remove_response = UpdateUserService.remove_user(user)
    response.status_code = remove_response.status_code
    return remove_response