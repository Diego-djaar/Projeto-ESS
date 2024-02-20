from fastapi import APIRouter, status, HTTPException
from src.schemas.response import HttpResponseModel
from src.service.impl.inventory_service import InventoryService
from src.service.impl.item_database_service import DadosItem

router = APIRouter()

# ok
@router.get(
    "/{CNPJ}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Visualização de todos os itens da loja",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Conteúdo do inventário obtido com sucesso"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha na obtenção do conteúdo do inventário"
        }
    },
)
def ver_inventario(CNPJ: str) -> HttpResponseModel:
    """ ver todos os itens do inventário """
    return InventoryService.get_items(cnpj = CNPJ)



# mudar quantidade de item
@router.post(
    "/{CNPJ}/atualizar_estoque",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Mudar quantidade de item",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Inventário atualizado"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha na atualização do inventário"
        }
    },
)
def modificar_quantidade_item(CNPJ: str, item_id:str) -> HttpResponseModel:
    """ Modifica quantidade disponível de determinado item """
    # TODO: verificação prévia: só pode modificar se item pertencer a CNPJ correto
    resultado = InventoryService.modify_item_quantity(item_id = item, qnt = qnt)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        raise HTTPException(
            status_code=resultado.status_code,
            detail=resultado.message
        )



# novo item
@router.post(
    "/{CNPJ}/adicionar_item",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Adiciona novo produto",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Inventário atualizado"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha na atualização do inventário"
        }
    },
)
def adicionar_item(
    id: str, 
    nome: str, 
    description: str, 
    price: str,
    quantidade: int,
    img : str,
    CNPJ: str, 
    ) -> HttpResponseModel:
    """ Cria novo item"""

    item_data = DadosItem(
        id = id,
        nome = nome,
        description = description,
        price = price,
        quantidade = quantidade,
        img = img
    )
        #inventory_service: add_new_item(item_data: DadosItem, cnpj : str, qnt : int)
    resultado = InventoryService.add_new_item(item_data = item_data, cnpj = CNPJ, qnt = quantidade)

    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        raise HTTPException(
            status_code = resultado.status_code,
            detail = resultado.message
        )


# TODO: deletar item, resetar base de dados