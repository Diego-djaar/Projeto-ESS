from fastapi import APIRouter, status, Response
from src.schemas.response import HttpResponseModel
import src.schemas.user_schemas as schemas
from src.service.impl.recuperation_service import RecuperationService

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
    description="Recuperar conta",
)
def recuperar_conta(email: str):
    RecuperationService.enviar_email(email)
    return {"message": f"Caso o email '{email}' esteja cadastrado enviaremos um código para o mesmo"}