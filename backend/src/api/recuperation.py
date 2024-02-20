from fastapi import APIRouter, status, Response
from schemas.response import HttpResponseModel
import schemas.user_schemas as schemas
from service.impl.recuperation_service import RecuperationService

router = APIRouter()

#Tela para digitar o email para receber o código
@router.get(
    "",
    status_code=status.HTTP_200_OK,
    description="Esqueci a senha",
)
def esqueci_a_senha():
    return {"message":"Vc esta na tela de esqueci a senha"}

#Rota para enviar o email digitado ao servidor
@router.post(
    "/enviarcodigo",
    status_code=status.HTTP_200_OK,
    description="Enviar código de recuperação",
)
def enviar_codigo(email: str):
    RecuperationService.enviar_email(email)
    return {"message": f"Caso o email '{email}' esteja cadastrado enviaremos um código para o mesmo"}

@router.post(
    "/recuperarconta",
    status_code=status.HTTP_200_OK,
    description="Digitar código de recuperação",
)
def recuperar_conta(email:str , codigo: str, nova_senha: str, nova_senha_repetida: str):
    message = RecuperationService.recuperar_conta(email, codigo, nova_senha, nova_senha_repetida)
    return {message}
