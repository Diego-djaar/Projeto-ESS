
from uuid import uuid4
from logging import INFO, WARNING, getLogger
import jsonpickle
import sys

if "pytest" in sys.modules:
    database_path = "Stores teste.json"
else:
    database_path = "Stores.json"

class Store(object):
    nome: str
    categoria: str
    email: str
    cnpj: str
    senha: str
    
    def new(CNPJ: str, Email: str, Senha: str, Categoria: str, Nome: str):
        obj = Store(CNPJ, Email, Senha, Categoria, Nome)
        return (obj)
    

    def __init__(self, CNPJ: str, Email: str, Senha: str, Categoria: str, Nome: str): 
        self.nome = Nome
        self.categoria = Categoria
        self.cnpj = CNPJ
        self.email = Email
        self.senha = Senha
    
        
    
    def update_data(self, dados_store: dict):
        self.nome = dados_store['nome']
        self.categoria = dados_store['categoria']
        self.email = dados_store['email']
        self.senha = dados_store['senha']
        
        return "Success"
    
    def update_password(self, dados_store: dict):
        self.senha = dados_store['senha']
        return "Success"
    
    def update_nome(self, dados_store: dict):
        self.nome = dados_store['nome']
        return "Success"
    
    def update_categoria(self, dados_store: dict):
        self.categoria = dados_store['categoria']
        return "Success"
    
    def update_email(self, dados_store: dict):
        self.email = dados_store['email']
        return "Success"



class StoreDatabase():
    db: dict[Store]
    file_path: str
    
    def signup(self, store: Store):
        success, reason = self.add_store(store)
        return (success, reason)
    
    
    def __init__(self, path = database_path):
        self.db = dict()
        self.file_path = path
        self.try_read_from_file()

    def try_read_from_file(self):
        # Ler stores de um arquivo
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
    

    def add_store(self, store: Store, update = True):
        reason = []
        if update:
            self.try_read_from_file()
        if self.get_store_by_cnpj(store.cnpj, False):
            reason.append("CNPJ")
        if reason.__len__() > 0:
            return (False, reason)
        
        self.db[store.cnpj] = store
        self.write_to_file()
        return (True, ["SUCCESS"])
    
    def get_store_by_cnpj(self, cnpj: str, update = True) -> Store | None:
        if update:
            self.try_read_from_file()
        return self.db.get(cnpj) 
    
    def get_store_by_name(self, name: str, update = True) -> Store | None:
        if update:
            self.try_read_from_file()
        for key, val in self.db.items():
            if val.email == name:
                return val
        return None
    
    def remove_store_by_cnpj(self, cnpj: str, update = True) -> Store | None:
        if update:
            self.try_read_from_file()
        toreturn = self.db.pop(cnpj, None)
        self.write_to_file()
        return toreturn
    
    def clear_database(self):
        self.db = dict()
        self.write_to_file()