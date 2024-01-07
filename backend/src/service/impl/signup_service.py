import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.__init__ import user_database as db
from src.db.user_database import User, UserDatabase
from src.schemas.user_response import HTTPSignUpResponses
from src.schemas.user_schemas import DadosCadastrais


class SingUpService():
    @staticmethod
    def signup_user(dados_cadastrais: DadosCadastrais, dbase = db) -> HttpResponseModel:
        """Tenta realizar o cadastro do usuário

        Args:
            dados_cadastrais (DadosCadastrais): _description_

        Returns:
            HttpResponseModel: _description_
        """
        (user, reason) = User.new(*dados_cadastrais.model_dump().values())
        if user == None:
            return HTTPSignUpResponses.BAD_REQUEST(reason)
        (success, reason) = dbase.signup(user)
        
        if success:
            return HTTPSignUpResponses.SIGNUP_SUCCESSFUL()
        else:
            if "CPF" in reason:
                return HTTPSignUpResponses.CPF_ALREADY_EXIST(reason)
            elif "USER" in reason:
                return HTTPSignUpResponses.USER_ALREADY_EXIST(reason)
        