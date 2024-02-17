import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.user_database import User, UserDatabase
from src.schemas.user_response import HTTPLoginResponses, HTTPVerifyResponses, HTTPUpdateUserResponses
from random import randrange
from bidict import bidict
from src.service.impl.__init__ import token_service
from src.schemas.user_schemas import DadosLogin, DadosUser
from test_singup_service import sign_up_user
from src.service.impl.auth_service import AuthService
from src.auth.token_service import TokenService
from src.schemas.user_schemas import DadosLogin, DadosUser
from src.db.__init__ import user_database_example as db
from src.service.impl.update_user_service import UpdateUserService

def test_remove_user():
    cpf1, cpf2, senha = sign_up_user(True)
    dados = DadosLogin(cpf_ou_user_ou_email=cpf1, senha=senha)
    token: str = AuthService.login_user(dados, db).data['token']
    dados_user = DadosUser.from_user(token_service.get_user_of_token(int(token)))
    
    assert dados_user is not None
    
    res = UpdateUserService.remove_user(dados_user, db)
    assert res == HTTPUpdateUserResponses.REMOVE(dados_user)
    
    res = UpdateUserService.remove_user(dados_user, db)
    assert res == HTTPUpdateUserResponses.REMOVE_FAIL()