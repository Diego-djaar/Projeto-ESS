from src.db.user_database import User, UserDatabase
import datetime
import jsonpickle
from bcrypt import hashpw, checkpw, gensalt
import hmac
import hashlib

def test_create_user():
    user = User.new(
        username="Enzo", 
        nome="Enzo Gabriel", 
        sobrenome="de Oliveira", 
        cpf="111.111.111-11", 
        data_de_nascimento=datetime.date.fromisocalendar(2001,1,1),
        email="ego@cin.ufpe.br", 
        senha="12345Abcx"
    )[0]
    assert user != None
    assert user.username == "Enzo"
    hash = hmac.new("111.111.111-11".encode(), "12345Abcx".encode(),  hashlib.sha512)
    assert checkpw(hash.digest(), user.senha)
    assert user.check_password("12345Abcx")

def test_user_bad_request():
    user, reason = User.new(
        username="Alisson", 
        nome="Enzo Gabriel", 
        sobrenome="de Oliveira", 
        cpf="54353", 
        data_de_nascimento=datetime.date.fromisocalendar(2001,1,1),
        email="", 
        senha="",
        CEP = ""
    )
    assert "CPF" in reason and "EMAIL" in reason and "SENHA" in reason and "CEP" in reason
    
    user, reason = User.new(
        username="Alisson", 
        nome="Enzo Gabriel", 
        sobrenome="de Oliveira", 
        cpf="543.535.123-67", 
        data_de_nascimento=datetime.date.fromisocalendar(2001,1,1),
        email="", 
        senha="",
        CEP = ""
    )
    assert "CPF" not in reason and "EMAIL" in reason and "SENHA" in reason and "CEP" in reason
    

def test_write_user_to_file():
    user = User.new(
        username="Enzo", 
        nome="Enzo Gabriel", 
        sobrenome="de Oliveira", 
        cpf="111.111.111-11", 
        data_de_nascimento=datetime.date.fromisocalendar(2001,1,1),
        email="ego@cin.ufpe.br", 
        senha="12345Abcx"
    )[0]
    user2 = User.new(
        username="Enzoo", 
        nome="Enzo Gabriel", 
        sobrenome="de Oliveira", 
        cpf="111.111.111-10", 
        data_de_nascimento=datetime.date.fromisocalendar(2001,1,1),
        email="ego@cin.ufpe.br", 
        senha="12345Abcx"
    )[0]
    database = UserDatabase("Usuários teste.json")
    database.add_user(user)
    database.add_user(user2)
    database.write_to_file()

def test_empty_database():
    database = UserDatabase("Usuários teste vazio.json")
    database.write_to_file()
    with open("Usuários teste vazio.json") as f:
        file = f.read()
        assert file == "{}"

def test_verify_user_from_database():
    # run test_write_user_to_file before this
    database = UserDatabase("Usuários teste.json")
    user = database.get_user_by_cpf("111.111.111-11")
    assert user.username == "Enzo"
    
    user = database.get_user_by_username("Enzoo")
    assert user.cpf == "111.111.111-10"
    
    user = database.get_user_by_cpf("0")
    assert user == None

def test_remove_user_from_database():
    user = User.new(
        username="Miguel", 
        nome="Miguel Guerra", 
        sobrenome="", 
        cpf="777.777.777-77", 
        data_de_nascimento=datetime.date.fromisocalendar(1,1,1),
        email="mg4@cin.ufpe.br", 
        senha="12345Abcx"
    )[0]
    database = UserDatabase("Usuários teste.json")
    database.add_user(user)
    
    assert database.get_user_by_cpf("777.777.777-77")
    
    database.remove_user_by_cpf("777.777.777-77")
    
    assert database.get_user_by_cpf("777.777.777-77") == None

def test_not_add_account_on_fail():
    database = UserDatabase("Usuários teste.json")
    database.remove_user_by_cpf("123.156.185-21")
    database.remove_user_by_cpf("123.156.184-21")
    user, reason = User.new(
        username = "stringw3532fgq",
        nome = "string",
        sobrenome="sting",
        cpf="123.156.185-21",
        data_de_nascimento=datetime.datetime(1,1,1),
        email="string@s",
        senha="string123",
        endereço="string",
        CEP="01010-142"
    )
    res, reas = database.add_user(user)
    
    dblen = database.db.__len__()
    
    assert res == True
    user2, reason2 = User.new(
        username = "stringw3532fgq",
        nome = "string",
        sobrenome="sting",
        cpf="123.156.184-21",
        data_de_nascimento=datetime.datetime(1,1,1),
        email="string@s",
        senha="string123",
        endereço="string",
        CEP="01010-142"
    )
    
    res, reas = database.add_user(user2)
    
    assert res == False
    
    assert dblen == database.db.__len__()
    