import datetime
from pydantic import BaseModel
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.db.__init__ import user_database_example as db
from src.db.user_database import User, UserDatabase
from src.schemas.user_response import HTTPSignUpResponses
import src.service.impl.signup_service as signup
import src.db.user_database as dbase

def sign_up_user(use_user):
    db.remove_user_by_cpf("123.123.123-45")
    db.remove_user_by_cpf("000.000.000-00")
    
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
    assert res1 == HTTPSignUpResponses.SIGNUP_SUCCESSFUL()
    assert res2 == HTTPSignUpResponses.CPF_ALREADY_EXIST(["CPF", "USER"]) or res2 == HTTPSignUpResponses.USER_ALREADY_EXIST(["CPF", "USER"])
    
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
    
    assert res3 == HTTPSignUpResponses.USER_ALREADY_EXIST(["USER"])
    if not use_user:
        db.remove_user_by_cpf("123.123.123-45")
        db.remove_user_by_cpf("000.000.000-00")
    else:
        return ("123.123.123-45", "000.000.000-00", "12345XyzW")


def test_signup_user():
    sign_up_user(False)

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
    
    assert res == HTTPSignUpResponses.BAD_REQUEST(["CPF"])

def test_good_request():
    dados_cadastrais = signup.DadosCadastrais(
        username= "Mariazinha",
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
    db.remove_user_by_cpf("000.000.000-00")