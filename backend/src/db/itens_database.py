from typing import List, Dict
from uuid import uuid4
from pymongo import MongoClient, errors
from pymongo.collection import Collection, IndexModel
#from src.config.config import env
from logging import INFO, WARNING, getLogger
from decimal import Decimal
import re

logger = getLogger('uvicorn')

class Item():
    """Classe que representa um item da database
    
        Criar com método new_item()

    Returns:
        (Item, "SUCCESS"), ou (None, reason) caso o input não seja validado.
        
        reason será o nome do campo rejeitado pela validação
    """
    id: int # Acessos a database serão pelo ID
    nome: str # Nome visível na interface
    description: str
    price: Decimal
    quantidade: int
    img: str | None # Path para o arquivo

    def is_image_path(path):
        # Função para verificar se o path é válido para evitar SQL injection
        # Ela considera extensões comuns de imagem e é case-insensitive (flag re.IGNORECASE)
        pattern = re.compile(r"^[^.\n]+\.(jpg|jpeg|png|gif|bmp|tiff)$", re.IGNORECASE)
        return re.match(pattern, path) is not None

    def new_item(id: str, nome: str, description: str, price: Decimal, quantidade: int, img: str | None):
        """Cria novo item no banco de dados, validando-o

        Args:
            id: str
            nome: str
            description: str
            price: Decimal -> Tipo para armazenar valores monetários
            quantidade: int
            img: str | None -> Path do arquivo

        Returns:
            (User, "SUCESS"), ou (None, reason) caso o input não seja validado.
            
            reason será a lista dos campos rejeitados pela validação. ["SUCCESS"] se o user for validado.
        """

        reason = []
        # Verifica se imagem tem um formato sustentado