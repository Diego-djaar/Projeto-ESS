import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.__init__ import user_database as db
from src.db.user_database import User, UserDatabase
from src.schemas.user_response import HTTPSignUpResponses, HTTPUpdateUserResponses
from src.schemas.user_schemas import DadosUser
from src.service.impl.auth_service import AuthService

class UpdateUserService():
    @staticmethod
    def remove_user(dados_user: DadosUser, dbase = db) -> HttpResponseModel:
        """Remove um usuário"""
        if dados_user is None:
            return HTTPUpdateUserResponses.REMOVE_FAIL()
        cpf = dados_user.cpf
        ret = dbase.remove_user_by_cpf(cpf)
        if ret is not None:
            return HTTPUpdateUserResponses.REMOVE(DadosUser.from_user(ret))
        else:
            return HTTPUpdateUserResponses.REMOVE_FAIL()