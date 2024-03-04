from fastapi import APIRouter, status, HTTPException
from src.schemas.response import HttpResponseModel
from src.service.impl.carrinho_service import Carrinho_service
from src.service.impl.item_database_service import DadosItem
from src.service.impl.carrinho_service import DadosEndereço

router = APIRouter()

@router.get(
    "/view/{CPF}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Visualização do carrinho",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Conteúdo do carrinho obtido com sucesso"
        },
        status.HTTP_201_CREATED: {
            "model":HttpResponseModel,
            "description": "Carrinho não encontrado, carrrinho criado"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha na obtenção do conteúdo do carrinho"
        }
    },
)
def visualizar_carrinho(CPF: str) -> HttpResponseModel:
    """ Se carrinho não for encontrado cria carrinho para o respectivo CPF """
    print("Entrou em visualizar carrinho")
    resultado = Carrinho_service.get_cart(CPF=CPF)
    return resultado

@router.post(
    "/adicionar",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Adicionar item ao carrinho",
    responses={
        status.HTTP_200_OK: {
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
    print("Entrou na função adicionar_item_ao_carrinho")
    print(dados)
    resultado = Carrinho_service.add_item_to_cart(item_data= dados, CPF= CPF)
    print(resultado)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        # Se a adição não foi bem-sucedida, lançar uma exceção HTTP que será tratada pelo FastAPI
        raise HTTPException(
            status_code=resultado.status_code,
            detail=resultado.message
        )
    
@router.delete(
    "/remover",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Remover item do carrinho",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Item removido do carrinho com sucesso"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha na remoção do item do carrinho"
        },
        status.HTTP_404_NOT_FOUND: {
            "model": HttpResponseModel,
            "description": "Item ou carrinho não encontrado"
        }
    },
)
def remover_item_do_carrinho(item_id: str, CPF: str) -> HttpResponseModel:
    """ Tenta remover item do carrinho """
    resultado = Carrinho_service.remove_item_from_cart(item_id=item_id, CPF=CPF)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        # Se a remoção não foi bem-sucedida, lançar uma exceção HTTP que será tratada pelo FastAPI
        raise HTTPException(
            status_code=resultado.status_code,
            detail=resultado.message
        )
    
@router.get(
    "/view_all_carts",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Visualização dos carrinhos",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Conteúdo dos carrinhos obtido com sucesso"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha na obtenção do conteúdo dos carrinhos"
        }
    },
)
def visualizar_carrinho() -> HttpResponseModel:
    """ Se carrinho não for encontrado cria carrinho para o respectivo CPF """
    return Carrinho_service.get_all_carts()

@router.delete(
    "/clear_cart",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Limpar carrinho",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Conteúdo do carrinho limpo com sucesso"
        },
        status.HTTP_404_NOT_FOUND: {
            "model": HttpResponseModel,
            "description": "Carrinho não encontrado"
        }
    },
)
def clear_cart(CPF: str) -> HttpResponseModel:
    """ Tenta limpar o carrinho """
    print("Entrou em clear_cart")
    resultado = Carrinho_service.clear_cart_by_CPF(CPF=CPF)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        raise HTTPException(
            status_code=resultado.status_code,
            detail=resultado.message
        )
    
@router.delete(
    "/clear_carts",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Limpar database de carrinhos",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Conteúdo da database limpo"
        }
    },
)
def clear_carts() -> HttpResponseModel:
    """ Tenta limpar a database de carrinhos """
    return Carrinho_service.clear_all_carts()

@router.put(
    "/incrementar_item",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Incrementar quantidade de item no carrinho",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Item incrementado com sucesso"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha no incremento da quantidade do item"
        },
        status.HTTP_404_NOT_FOUND: {
            "model": HttpResponseModel,
            "description": "Carrinho ou item não encontrado"
        }
    },
)
def incrementar_item (item_id: str, CPF: str) -> HttpResponseModel:
    """ Tenta Incrementar quantidade de item no carrinho """
    resultado = Carrinho_service.increase_item_quantity(item_id=item_id, CPF=CPF)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        # Se a adição não foi bem-sucedida, lançar uma exceção HTTP que será tratada pelo FastAPI
        raise HTTPException(
            status_code=resultado.status_code,
            detail=resultado.message
        )


@router.put(
    "/decrementar_item",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Decrementar quantidade de item no carrinho",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Item decrementado com sucesso"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha no decremento da quantidade do item"
        },
        status.HTTP_404_NOT_FOUND: {
            "model": HttpResponseModel,
            "description": "Carrinho ou item não encontrado"
        }
    },
)
def decrementar_item (item_id: str, CPF: str) -> HttpResponseModel:
    """ Tenta decrementar quantidade de item no carrinho """
    resultado = Carrinho_service.decrease_item_quantity(item_id=item_id, CPF=CPF)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        # Se a adição não foi bem-sucedida, lançar uma exceção HTTP que será tratada pelo FastAPI
        raise HTTPException(
            status_code=resultado.status_code,
            detail=resultado.message
        )

@router.put(
    "/alterar_endereço",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Alterar endereço do carrinho",
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Item adicionado ao carrinho com sucesso"
        },
        status.HTTP_400_BAD_REQUEST: {
            "model": HttpResponseModel,
            "description": "Falha na adição do item ao carrinho"
        }
    },
)
def alterar_endereço(dados: DadosEndereço, CPF: str) -> HttpResponseModel:
    """ Tenta adicionar item ao carrinho """
    resultado = Carrinho_service.add_adress(dados, CPF)
    if resultado.status_code == status.HTTP_200_OK:
        return resultado
    else:
        # Se a adição não foi bem-sucedida, lançar uma exceção HTTP que será tratada pelo FastAPI
        raise HTTPException(
            status_code=resultado.status_code,
            detail=resultado.message
        )
