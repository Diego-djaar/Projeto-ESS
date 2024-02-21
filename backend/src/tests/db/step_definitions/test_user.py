from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.db.__init__ import user_database
from src.db.user_database import User
from pytest_bdd import parsers, given, when, then, scenario
import datetime
import pytest
from src.db.user_database import User, UserDatabase
from bcrypt import hashpw, checkpw, gensalt


@pytest.fixture(scope="session", autouse=True)
def database_setup():
    user_database.remove_user_by_cpf("123.156.185-21")

"""Scenario: Criação de novo usuário"""
@scenario(scenario_name="Criação de novo usuário", feature_name="../features/user.feature")
def test_user():
    """User creation"""
    
"""Scenario: Criação de novo usuário falha"""
@scenario(scenario_name="Criação de novo usuário falha", feature_name="../features/user.feature")
def test_user_fail():
    """User creation fail"""
    
"""Scenario: Adição do usuário a base de dados"""
@scenario(scenario_name="Adição do usuário a base de dados", feature_name="../features/user.feature")
def test_add_user_to_db():
    """Add user to database"""

@when(
    parsers.cfparse('é criado um novo user com os dados User(username="{username}", nome="{nome}", sobrenome="{sobrenome}", cpf="{cpf}", data_de_nascimento="{data_de_nascimento}", email="{email}", senha="{senha}")'),
    target_fixture="created_user_reason"
)
def create_user(username: str, nome: str, sobrenome: str, cpf: str, data_de_nascimento: str, email: str, senha: str):
    data_de_nascimento = eval(data_de_nascimento)
    user_reason = User.new(
        username=username, 
        nome=nome, 
        sobrenome=sobrenome, 
        cpf=cpf, 
        data_de_nascimento=data_de_nascimento,
        email=email, 
        senha=senha
    )
    return user_reason


@when(
    parsers.cfparse('é criado um novo user com os dados User(username="{username}", nome="{nome}", sobrenome="{sobrenome}", cpf="{cpf}", data_de_nascimento="{data_de_nascimento}", email="{email}", senha="{senha}", endereço="{endereço}", CEP="{cep}"")'),
    target_fixture="created_user_reason"
)
def create_user_2(username: str, nome: str, sobrenome: str, cpf: str, data_de_nascimento: str, email: str, senha: str, endereço: str, cep: str):
    data_de_nascimento = eval(data_de_nascimento)
    user_reason = User.new(
        username=username, 
        nome=nome, 
        sobrenome=sobrenome, 
        cpf=cpf, 
        data_de_nascimento=data_de_nascimento,
        email=email, 
        senha=senha,
        endereço=endereço,
        cep=cep
    )
    return user_reason

@then("a criação do user é bem sucedida")
def check_user(created_user_reason):
    assert created_user_reason[0] is not None
    
@then("a criação do user é mal sucedida")
def check_user(created_user_reason):
    assert created_user_reason[0] is None
    
@then(parsers.cfparse('o user possui a senha "{senha}"'))
def check_senha(senha: str, created_user_reason):
    assert created_user_reason[0].check_password(senha)

@then(parsers.cfparse('"{campo}" está na razão da falha'))
def check_reason(campo: str, created_user_reason):
    assert campo in created_user_reason[1]

@when('o user é adicionado a base de dados')
def add_user_to_db(created_user_reason):
    user: User = created_user_reason[0]
    assert user_database.add_user(user)[0]

@then(parsers.cfparse('Usuário "{username}" está cadastrado'))
def check_db(username: str):
    assert user_database.get_user_by_username(username)