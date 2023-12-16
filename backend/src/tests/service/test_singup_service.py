import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.__init__ import user_database_example as db
from src.db.user_database import User, UserDatabase
from src.schemas.signup_response import HTTPSignUpResponses
import src.service.impl.signup_service as signup
import src.db.user_database as dbase

def test_signup_user():
    dados_cadastrais = signup.DadosCadastrais(
        username= "Maria",
        nome = "Maria",
        sobrenome = "Agra",
        cpf = "123.123.123-45",
        data_de_nascimento=datetime.datetime(1999,12,31),
        email="Maria@proton.me",
        senha="12345XyzW",
        endereço = None,
        CEP = None
    )
    res1 = signup.SingUpService.signup_user(dados_cadastrais, db)
    res2 = signup.SingUpService.signup_user(dados_cadastrais, db)
    
    assert res2 == HTTPSignUpResponses.CPF_ALREADY_EXIST() or res2 == HTTPSignUpResponses.USER_ALREADY_EXIST()
    
    dados_cadastrais = signup.DadosCadastrais(
        username= "Maria",
        nome = "Maria",
        sobrenome = "Agra",
        cpf = "000.000.000-00",
        data_de_nascimento=datetime.datetime(1999,12,31),
        email="Maria@proton.me",
        senha="12345XyzW",
        endereço = None,
        CEP = None
    )
    
    res3 = signup.SingUpService.signup_user(dados_cadastrais, db)
    
    assert res3 == HTTPSignUpResponses.USER_ALREADY_EXIST()
    
    db.remove_user_by_cpf("123.123.123-45")
    db.remove_user_by_cpf("000.000.000-00")

def test_bad_request():
    dados_cadastrais = signup.DadosCadastrais(
        username= "Maria",
        nome = "Maria",
        sobrenome = "Agra",
        cpf = "bad",
        data_de_nascimento=datetime.datetime(1999,12,31),
        email="Maria@proton.me",
        senha="12345XyzW",
        endereço = None,
        CEP = None
    )
    res = signup.SingUpService.signup_user(dados_cadastrais, db)
    
    assert res == HTTPSignUpResponses.BAD_REQUEST("CPF")

def test_good_request():
    dados_cadastrais = signup.DadosCadastrais(
        username= "Maria",
        nome = "Maria",
        sobrenome = "Agra",
        cpf = "000.000.000-00",
        data_de_nascimento=datetime.datetime(1999,12,31),
        email="Maria@proton.me",
        senha="12345XyzW",
        endereço = None,
        CEP = None
    )
    db.remove_user_by_cpf("000.000.000-00")
    
    res = signup.SingUpService.signup_user(dados_cadastrais, db)
    assert res == HTTPSignUpResponses.SIGNUP_SUCCESSFUL()