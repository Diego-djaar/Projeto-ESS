from src.db.__init__ import user_database_example as db
from src.db.__init__ import recuperacao_database_test as db_recuperacao
from src.db.codigos_rec_database import Recuperacao
from src.service.impl.recuperation_service import RecuperationService
from datetime import datetime, timedelta
import pytest
import src.service.impl.signup_service as signup
from unittest.mock import patch, MagicMock
from src.db.__init__ import user_database
from src.db.user_database import User
from pytest_bdd import parsers, given, when, then, scenario
import pytest
from src.main import app
from src.schemas.user_schemas import DadosLogin, DadosUser
from src.service.impl.auth_service import AuthService
from src.schemas.user_response import HTTPLoginResponses, HTTPVerifyResponses

@pytest.fixture(scope="module", autouse=True)
def user_valido():
    dados_cadastrais = signup.DadosCadastrais(
        username="Peterson", 
        nome = "Peterson", 
        sobrenome="Melo", 
        cpf="111.111.111-02", 
        data_de_nascimento=datetime(2003,5,29), 
        email="djaar@cin.ufpe.br", 
        senha="faculdade123", 
        endereço= "Rua tal", 
        CEP="50000-000"
    )
    
    signup.SingUpService.signup_user(dados_cadastrais, db)

    user = db.get_user_by_email("djaar@cin.ufpe.br")

    yield user

    db.clear_database()
    db_recuperacao.clear_database()

# Função para fornecer um código válido para os testes
def codigo_valido(email):
    codigo = db_recuperacao.get_rec_by_email(email).codigo
    return codigo

"""Scenario: Logar após recuperar Senha"""
@scenario(scenario_name="Logar após recuperar Senha", feature_name="../features/integrate_login_recuperarsenha.feature")
def test_login_recovery():
    """Login after email recovery"""
    
@given(parsers.cfparse('Usuário com Cpf "{cpf}" não está cadastrado'))
def check_cpf(cpf: str):
    assert user_database.get_user_by_cpf(cpf) is None
    
@then(parsers.cfparse('Usuário com Cpf "{cpf}" está cadastrado'),
target_fixture="user_")
@given(parsers.cfparse('Usuário com Cpf "{cpf}" está cadastrado'),
target_fixture="user_")
def check_cpf(cpf: str):
    user = user_database.get_user_by_cpf(cpf)
    assert user is not None
    return user

@then(parsers.cfparse('o usuário possui a senha "{senha}"'))
@given(parsers.cfparse('o usuário possui a senha "{senha}"'))
def check_psw(senha: str, user_: User):
    assert user_.check_password(senha)
    
@when(parsers.cfparse('o método Login User é chamado com DadosLogin(cpf_ou_user_ou_email="{cpf}", senha="{senha}")'),
target_fixture="response")
def login(cpf: str, senha: str):
    dados = DadosLogin(cpf_ou_user_ou_email=cpf, senha=senha)
    res = AuthService.login_user(dados)
    return res

@then('o método deve retornar que o login foi bem sucedido')
def check_success(response):
    assert response.message == "Login com sucesso"

@then('o método deve retornar que o login foi mal sucedido')
def check_fail(response):
    assert response == HTTPLoginResponses.LOGIN_FAILED() or response == HTTPLoginResponses.USER_NOT_FOUND()

@then(parsers.cfparse('o campo "{campo}" da resposta deve conter o valor "{value}"'))
def check_value(campo: str, value: str, response):
    assert getattr(response, campo) == value
    
@then(parsers.cfparse('o campo "{campo1}" da resposta deve conter o campo "{campo2}"'))
def check_field(campo1: str, campo2: str, response):
    assert getattr(response, campo1)[campo2]

@given(parsers.cfparse('o usuário possui o campo "{campo}" o valor "{value}"'))
def check_value_in_user(campo: str, value: str, user_: User):
    assert getattr(user_, campo) == value

@when(parsers.cfparse('o método Enviar Email é chamado com email: "{email}"'))
def email_send(email: str):
    assert RecuperationService.enviar_email(email, db_user=db, db_recuperacao=db_recuperacao) == True

@when(parsers.cfparse('o método Recuperar Conta é chamado com email: "{email}", código válido e nova senha "{senha}"'))
def recovery_account(email: str, senha: str):
    assert RecuperationService.recuperar_conta(email, codigo_valido(email), senha, senha, db_user=db, db_recuperacao=db_recuperacao) == True    

