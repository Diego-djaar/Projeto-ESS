from src.db.user_database import User, UserDatabase
import datetime
import jsonpickle
from bcrypt import hashpw, checkpw, gensalt
import hmac
import hashlib

def test_create_user():
    user = User(
        username="Enzo", 
        nome="Enzo Gabriel", 
        sobrenome="de Oliveira", 
        cpf="111.111.111-11", 
        data_de_nascimento=datetime.date.fromisocalendar(2001,1,1),
        email="ego@cin.ufpe.br", 
        senha="12345Abcx"
    )
    assert user != None
    assert user.username == "Enzo"
    hash = hmac.new("111.111.111-11".encode(), "12345Abcx".encode(),  hashlib.sha512)
    assert checkpw(hash.digest(), user.senha)
    assert user.check_password("12345Abcx")

def test_write_user_to_file():
    user = User(
        username="Enzo", 
        nome="Enzo Gabriel", 
        sobrenome="de Oliveira", 
        cpf="111.111.111-11", 
        data_de_nascimento=datetime.date.fromisocalendar(2001,1,1),
        email="ego@cin.ufpe.br", 
        senha="12345Abcx"
    )
    user2 = User(
        username="Enzoo", 
        nome="Enzo Gabriel", 
        sobrenome="de Oliveira", 
        cpf="111.111.111-10", 
        data_de_nascimento=datetime.date.fromisocalendar(2001,1,1),
        email="ego@cin.ufpe.br", 
        senha="12345Abcx"
    )
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
    