import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.__init__ import user_database as db
from src.db.user_database import User, UserDatabase
from src.schemas.user_response import HTTPLoginResponses
from random import randrange
from bidict import bidict
from src.auth.token_service import TokenService

def test_add_user():
    token_service = TokenService()
    
    user, reason = User.new(
        username="Enzo",
        nome="Enzo",
        sobrenome="Gabriel",
        cpf="111.222.333-44",
        data_de_nascimento=datetime.datetime(1804,2,29),
        email="enzo@e",
        senha="1234abcd"
    )
    assert not token_service.user_active(12345)
    assert token_service.get_user_of_token(12345) == None
    
    token = token_service.add_user(user)
    
    assert token_service.user_active(token)
    assert token_service.get_user_of_token(token) == user
    
    token_service.clear()
    
    assert not token_service.user_active(token)
    assert token_service.get_user_of_token(token) == None
    
def test_rm_user():
    token_service = TokenService()
    
    user, reason = User.new(
        username="Enzo",
        nome="Enzo",
        sobrenome="Gabriel",
        cpf="111.222.333-44",
        data_de_nascimento=datetime.datetime(1804,2,29),
        email="enzo@e",
        senha="1234abcd"
    )
    
    token = token_service.add_user(user)
    
    assert token_service.user_active(token)
    assert token_service.get_user_of_token(token) == user
    
    token_service.rm_user(token=token)
    
    
    assert not token_service.user_active(token)
    assert token_service.get_user_of_token(token) == None
    
    token = token_service.add_user(user)
    
    assert token_service.user_active(token)
    assert token_service.get_user_of_token(token) == user
    
    token_service.rm_user(user=user)
    
    assert not token_service.user_active(token)
    assert token_service.get_user_of_token(token) == None
    
def test_multi_add():
    token_service = TokenService()
    user1, reason = User.new(
        username="Enzo",
        nome="Enzo",
        sobrenome="Gabriel",
        cpf="111.222.333-44",
        data_de_nascimento=datetime.datetime(1804,2,29),
        email="enzo@e",
        senha="1234abcd"
    )
    user2, reason = User.new(
        username="Enzo0",
        nome="Enzo",
        sobrenome="Gabriel",
        cpf="111.222.333-45",
        data_de_nascimento=datetime.datetime(1804,2,29),
        email="enzo@e",
        senha="1234abcd"
    )
    user3, reason = User.new(
        username="Enzo0",
        nome="Enzo",
        sobrenome="Gabriel",
        cpf="111.222.333-46",
        data_de_nascimento=datetime.datetime(1804,2,29),
        email="enzo@e",
        senha="1234abcd"
    )
    
    token1 = token_service.add_user(user1)
    token2 = token_service.add_user(user2)
    token3 = token_service.add_user(user3)
    
    assert token_service.user_active(token1)
    assert token_service.user_active(token2)
    assert token_service.user_active(token3)
    
    assert token_service.get_user_of_token(token1) == user1
    assert token_service.get_user_of_token(token2) == user2
    assert token_service.get_user_of_token(token3) == user3
    
    token_service.rm_user(token=token2)
    
    assert token_service.user_active(token1)
    assert not token_service.user_active(token2)
    assert token_service.user_active(token3)
    
    assert token_service.get_user_of_token(token1) == user1
    assert token_service.get_user_of_token(token2) == None
    assert token_service.get_user_of_token(token3) == user3
    
    token4 = token_service.add_user(user2)
    
    assert token2 != token4
    
    assert token_service.user_active(token1)
    assert not token_service.user_active(token2)
    assert token_service.user_active(token3)
    assert token_service.user_active(token4)
    
    assert token_service.get_user_of_token(token1) == user1
    assert token_service.get_user_of_token(token2) == None
    assert token_service.get_user_of_token(token3) == user3
    assert token_service.get_user_of_token(token4) == user2
    
    
    