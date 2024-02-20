import datetime
from pydantic import BaseModel
from schemas.response import HTTPResponses, HttpResponseModel
from db.__init__ import user_database as db
from db.user_database import User, UserDatabase
from schemas.user_response import HTTPSignUpResponses, HTTPUpdateUserResponses
from schemas.user_schemas import DadosUser
from service.impl.auth_service import AuthService
from service.impl.__init__ import token_service

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
    
    @staticmethod
    def update_user(token_user: "str", new_user_data: DadosUser, dbase = db) -> HttpResponseModel:
        """Atualiza os dados de usuário"""
        # Recupera usuário pelo serviço de token
        old_user = token_service.get_user_of_token(int(token_user))
        if old_user is None:
            return HTTPUpdateUserResponses.UNAUTORIZED()
        
        # Valida se a atualização é válida conforme o especificado
        if old_user.cpf != new_user_data.cpf or old_user.email != new_user_data.email or old_user.username != new_user_data.username:
            reason = ["Tried to update CPF, EMAIL or USERNAME"]
            return HTTPUpdateUserResponses.UPDATE_FAIL(reason)
        
        # Tenta atualizar o usuário
        reason = old_user.update_data(new_user_data.model_dump())
        print(reason)
        if not "SUCCESS" in reason:
            return HTTPUpdateUserResponses.UPDATE_FAIL(reason)
        
        # Atualiza a base de dados no disco
        dbase.write_to_file()
        
        return HTTPUpdateUserResponses.UPDATE_SUCCESS()
