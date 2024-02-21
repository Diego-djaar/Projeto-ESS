from fastapi import APIRouter, status, HTTPException
from src.schemas.response import HttpResponseModel
from src.service.impl.store_service import Store_service, DadosLoja, DadosLoginLoja, DadosRetrieveLoja, DadosChangeLoja

router = APIRouter()

@router.post(
    "/signup",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Cadastro do usuario",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Cadastro realizado de forma de bem sucedida"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Cadastro não realizado"
        }
    },
)
def store_signup(dados: DadosLoja):
    """Se a loja ainda não estiver cadastrada, adiciona ela na db"""
    resultado = Store_service.signup_store(dados)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        raise HTTPException(status_code=resultado.status_code, detail=resultado.message)



@router.post(
    "/login",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Login do usuario",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Login realizado de forma de bem sucedida"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Login não realizado"
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": HttpResponseModel,
            "description": "CNPJ ou Senha incorretos"
        },
    },
)
def store_login(dados: DadosLoginLoja):
    """Se os dados de entrada corresponderem com a db redireciona usuario para homepage"""
    resultado = Store_service.login_store(dados)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        raise HTTPException(status_code=resultado.status_code, detail=resultado.message)
    


@router.post(
    "/login/retrieve_password",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Recuperação de Senha",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Senha redefinida com sucesso"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Senha não pode ser redefinida"
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": HttpResponseModel,
            "description": "CPNJ não registrado"
        },
    },
)
def store_retrieve_password(dados: DadosRetrieveLoja):
    """Se CNPJ e Email estiverem no bd, redefine a senha do usuario"""
    resultado = Store_service.retrieve_password(dados)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        raise HTTPException(status_code=resultado.status_code, detail=resultado.message)
    
@router.post(
    "/store/change_store_data",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Modifição de dados da loja",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Dados atualizados com sucesso"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Dados não foram atualizados"
        },
    },
)
def change_store_data(dados:DadosChangeLoja):
    """Se CNPJ e Email estiverem no bd, redefine a senha do usuario"""
    resultado = Store_service.change_user_data(dados)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        raise HTTPException(status_code=resultado.status_code, detail=resultado.message)