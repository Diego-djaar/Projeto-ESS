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
    # Registra usuário
    cpf1, cpf2, senha = sign_up_user(True)
    dados = DadosLogin(cpf_ou_user_ou_email=cpf1, senha=senha)
    token: str = AuthService.login_user(dados, db).data['token']
    
    # Verifica retorno ao verificar vs deslogar
    dados_user = DadosUser.from_user(token_service.get_user_of_token(int(token)))
    dados_user_0 = AuthService.unlogin_user_internal(token)
    assert dados_user == dados_user_0
    assert dados_user is not None
    
    # Testa retorno ao remover usuário
    res = UpdateUserService.remove_user(dados_user, db)
    assert res == HTTPUpdateUserResponses.REMOVE(dados_user)
    
    # Testa retorno ao ver se o usuário permanece logado
    res_get_user =  token_service.get_user_of_token(int(token))
    assert res_get_user == None
    
    # Testa se usuário está na database
    res_user_in_db = db.get_user_by_cpf(dados_user.cpf)
    assert res_user_in_db == None
    
    # Testa falha ao tentar remover de novo
    res = UpdateUserService.remove_user(dados_user, db)
    assert res == HTTPUpdateUserResponses.REMOVE_FAIL()

def test_update_user():
     # Registra usuário
    cpf1, cpf2, senha = sign_up_user(True)
    dados = DadosLogin(cpf_ou_user_ou_email=cpf1, senha=senha)
    token: str = AuthService.login_user(dados, db).data['token']
    
    dados_user: DadosUser = DadosUser.from_user(token_service.get_user_of_token(int(token)))
    
    res = UpdateUserService.update_user(token, dados_user, db)
    assert res==HTTPUpdateUserResponses.UPDATE_SUCCESS()
    
    dados_user2 = dados_user.model_copy()
    dados_user2.cpf = "999.999.999-99"
    res = UpdateUserService.update_user(token, dados_user2, db)
    assert res == HTTPUpdateUserResponses.UPDATE_FAIL(["Tried to update CPF, EMAIL or USERNAME"])
    
    dados_user3 = dados_user.model_copy()
    dados_user3.CEP = "12654-456"
    res = UpdateUserService.update_user(token, dados_user3)
    assert res==HTTPUpdateUserResponses.UPDATE_SUCCESS()
    
    dados_user_new: DadosUser = DadosUser.from_user(token_service.get_user_of_token(int(token)))
    assert dados_user_new.cpf == dados_user.cpf
    assert dados_user_new.CEP != dados_user.CEP
    assert dados_user_new.__dict__ == dados_user3.__dict__