from typing import List, Dict
from uuid import uuid4
from pymongo import MongoClient, errors
from pymongo.collection import Collection, IndexModel
#from config.config import env
from logging import INFO, WARNING, getLogger
import datetime
from bcrypt import hashpw, checkpw, gensalt
import hmac
import hashlib
import re
import jsonpickle
import sys

# Faz os testes não interferirem com o funcionamento do programa em live
if "pytest" in sys.modules:
    database_path = "Usuários teste.json"
else:
    database_path = "Usuários.json"

logger = getLogger('uvicorn')

cpf_pattern = re.compile(r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$")
cep_pattern = re.compile(r"^[0-9]{5}\-[0-9]{3}$")
email_pattern = re.compile(r"^[\w\.]+@[\w\.]+$")
senha_pattern = re.compile(r"(?=.{8,})(?=.*[0-9].*)(?=.*[a-zA-Z].*)")
username_pattern = re.compile(r"([a-z]|[A-Z]| |_|[0-9])*$")

class User(object):
    """Classe que representa um usuário do ecommerce
    
        Criar com método new()

    Returns:
        (User, "SUCCESS), ou (None, reason) caso o input não seja validado.
        
        reason será o nome do campo rejeitado pela validação
    """
    username: str
    nome: str
    sobrenome: str
    cpf: str
    endereço: str | None
    CEP: str | None
    data_de_nascimento: datetime.date
    email: str
    senha: bytes
    id: int
    
    def new(username: str, nome: str, sobrenome: str, cpf: str, data_de_nascimento: datetime.date, email: str, senha: str, 
        endereço: str | None = None, CEP: str | None = None):
        """Cria novo usuário, validando-o

        Args:
            username (str): str
            nome (str): str
            sobrenome (str): str
            cpf (str): "DDD.DDD.DDD-DD"
            data_de_nascimento (datetime.date): formato datetime
            email (str): ter 1 @
            senha (str): pelo menos 8 caracters, 1 letra e 1 número
            endereço (str | None, optional): Defaults to None.
            CEP (str | None, optional): Defaults to None.

        Returns:
            (User, reason), ou (None, reason) caso o input não seja validado.
            
            reason será a lista dos campos rejeitados pela validação. ["SUCCESS"] se o user for validado.
        """
        reason = []
        if not cpf_pattern.match(cpf):
            reason.append("CPF")
        if not (CEP is None) and not (cep_pattern.match(CEP)):
            reason.append("CEP")
        if not email_pattern.match(email):
            reason.append("EMAIL")
        if not senha_pattern.match(senha):
            reason.append("SENHA")
        if not username_pattern.match(username):
            reason.append("USERNAME")
            
        obj = None
        if reason.__len__() == 0:
            reason.append("SUCCESS")
            obj = User(username, nome, sobrenome, cpf, data_de_nascimento, email, senha,endereço, CEP)
            
        return (obj, reason)
    
    def __init__(self, username: str, nome: str, sobrenome: str, cpf: str, data_de_nascimento: datetime.date, email: str, senha: str, 
                endereço: str | None = None, CEP: str | None = None): 
        self.username = username
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.endereço = endereço
        self.CEP = CEP
        self.data_de_nascimento = data_de_nascimento
        self.email = email
        self.add_password(senha)
        self.id = abs(hash((datetime.datetime.now(), self.cpf, self.username)))
    
    def add_password(self, senha: str):
        """Atualiza a senha do usuário

        Args:
            senha (str): Senha em formato de string. Não deve ser armazenada em hipótese alguma.
        """
        hash = self.cpf.encode() + senha.encode()
        self.senha = hashpw(hash, gensalt())
        
    def check_password(self, senha: str):
        """Verifica se essa senha é a do usuário

        Args:
            senha (str): Senha em formato de string. Não deve ser armazenada em hipótese alguma.

        Returns:
            True se é, ou False se não é
        """
        hash = self.cpf.encode() + senha.encode()
        return checkpw(hash, self.senha)
    
    def update_data(self, dados_user: dict):
        """Atualiza os dados do usuário
        
        OBS: Sempre chame UserDatabase.write_to_file() para atualizar os dados do usuário na base de dados
        """
        reason = []
        if not (dados_user['CEP'] is None) and not (cep_pattern.match(dados_user['CEP'])):
            reason.append("CEP in wrong format")
        
        if reason.__len__() > 0:
            return reason
            
        self.nome = dados_user['nome']
        self.sobrenome = dados_user['sobrenome']
        self.endereço = dados_user['endereço']
        self.CEP = dados_user['CEP']
        self.data_de_nascimento = dados_user['data_de_nascimento']
        
        reason.append("SUCCESS")
        return reason

        

        

class UserDatabase():
    db: dict[User]
    file_path: str
    
    def signup(self, user: User):
        """Alias para add_user"""
        success, reason = self.add_user(user)
        return (success, reason)
    
    
    def __init__(self, path = database_path):
        self.db = dict()
        self.file_path = path
        self.try_read_from_file()

    def try_read_from_file(self):
        # Ler users de um arquivo
        import os.path
        if not os.path.exists(self.file_path):
            self.write_to_file()
            return None
        
        with open(self.file_path) as f:
            objetos = f.read()
            try:
                db = jsonpickle.decode(objetos)
            except:
                print("corrupted or wrong database")
                self.write_to_file()
            if type(db) == dict:
                self.db = db

    def write_to_file(self):
        objetos = jsonpickle.encode(self.db)
        with open(self.file_path, 'w+') as f:
            f.write(objetos)
    

    def valid_password(self, senha:str):
        return senha_pattern.match(senha)

    def add_user(self, user: User, update = True):
        """Adicionar um novo usuário a database

        Args:
            user (User): Usuário em questão
            
        Returns:
            success (bool): True para cadastro bem sucedido, False para mal sucedido
            reason (list[str]): contém "CPF" se a razão for um CPF já existente, contém "USER" se for um user já existente.
            ["SUCCESS"] caso tenha sido um cadastro bem sucedido
        """
        reason = []
        if update:
            self.try_read_from_file()
        if self.get_user_by_cpf(user.cpf, False):
            reason.append("CPF")
        if self.get_user_by_username(user.username, False):
            reason.append("USER")
        if self.get_user_by_email(user.email, False):
            reason.append("EMAIL")
        if reason.__len__() > 0:
            return (False, reason)
        
        self.db[user.cpf] = user
        self.write_to_file()
        return (True, ["SUCCESS"])
    
    def get_user_by_cpf(self, cpf: str, update = True) -> User | None:
        """Pega um usuário da database por cpf. Esse é o método mais eficiente.

        Args:
            cpf (str): Cpf do usuário

        Returns:
            User | None: Usuário retornado
        """
        if update:
            self.try_read_from_file()
        return self.db.get(cpf)
    
    def get_user_by_username(self, username: str, update = True) -> User | None:
        """Pega um usuário da database por username.

        Args:
            username (str): Username do usuário

        Returns:
            User | None: Usuário retornado
        """
        if update:
            self.try_read_from_file()
        for key, val in self.db.items():
            if val.username == username:
                return val
        return None
    
    def get_user_by_email(self, email: str, update = True) -> User | None:
        """Pega um usuário da database por email.

        Args:
            email (str): Email do usuário

        Returns:
            User | None: Usuário retornado
        """
        if update:
            self.try_read_from_file()
        for key, val in self.db.items():
            if val.email == email:
                return val
        return None
    
    def get_user_by_id(self, id: int, update = True) -> User | None:
        """Pega um usuário da database por id.

        Args:
            username (str): Id do usuário

        Returns:
            User | None: Usuário retornado
        """
        if update:
            self.try_read_from_file()
        for key, val in self.db.items():
            if val.id == id:
                return val
        return None
        
    def get_user_list(self, update = True) -> list[User]:
        """Retorna a lista de todos os usuários no ecommerce
        """
        if update:
            self.try_read_from_file()
        return list(self.db.values())
    
    def remove_user_by_cpf(self, cpf: str, update = True) -> User | None:
        """Remove o usuário de respectivo CPF

        Args:
            cpf (str): CPF do usuário a ser removido

        Returns:
            User | None: Retorna o User removido, ou None se nenhum foi removido
        """
        if update:
            self.try_read_from_file()
        toreturn = self.db.pop(cpf, None)
        self.write_to_file()
        return toreturn
    
    def clear_database(self):
        self.db = dict()
        self.write_to_file()
        
