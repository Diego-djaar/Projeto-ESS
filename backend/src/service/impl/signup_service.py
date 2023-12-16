import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.__init__ import user_database as db
from src.db.user_database import User, UserDatabase
from src.schemas.signup_response import HTTPSignUpResponses

class DadosCadastrais(BaseModel):
    username: str
    nome: str
    sobrenome: str
    cpf: str
    data_de_nascimento: datetime.date
    email: str
    senha: str
    endereço: str | None
    CEP: str | None

class SingUpService():
    @staticmethod
    def signup_user(dados_cadastrais: DadosCadastrais, dbase = db) -> HttpResponseModel:
        """Tenta realizar o cadastro do usuário

        Args:
            dados_cadastrais (DadosCadastrais): _description_

        Returns:
            HttpResponseModel: _description_
        """
        (success, reason) = dbase.signup(User(*dados_cadastrais.model_dump().values()))
        
        # Depois, alguma coisa assim, com base no resultado da operação
        if success:
            return HTTPSignUpResponses.SIGNUP_SUCCESSFUL()
        else:
            if reason == "CPF":
                return HTTPSignUpResponses.CPF_ALREADY_EXIST()
            elif reason == "USER":
                return HTTPSignUpResponses.USER_ALREADY_EXIST()
        