from src.schemas.response import HttpResponseModel
from pydantic import BaseModel
from src.db.__init__ import store_database as db
from src.db.store_database import Store
from src.schemas.store_response import HTTPSignUpResponses, HTTPLoginResponses, HTTPUpdateStoreResponses

class DadosLoja(BaseModel):
    cnpj: str
    email: str
    senha: str
    categoria: str
    nome: str

class DadosLoginLoja(BaseModel):
    cnpj: str
    senha: str

class DadosRetrieveLoja(BaseModel):
    cnpj: str
    email: str
    nsenha: str


class DadosChangeLoja(BaseModel):
    cnpj: str
    nemail: str | None
    senha: str
    nsenha: str | None
    ncategoria: str | None
    nnome: str | None
   

class Store_service():

    @staticmethod
    def signup_store(dados: DadosLoja, database = db) -> HttpResponseModel:
        """Tentar registrar uma nova loja"""
        store = Store.new(*dados.model_dump().values())
        if store == None:
            return HTTPSignUpResponses.BAD_REQUEST()
        success, r = database.signup(store)
        if success:
            return HTTPSignUpResponses.SIGNUP_SUCCESSFUL()
        else:
            return HTTPSignUpResponses.ALREADY_EXIST()
        


    @staticmethod
    def login_store(dados: DadosLoginLoja, database = db) -> HttpResponseModel:
        CNPJ = dados.cnpj
        Senha = dados.senha
        store = database.get_store_by_cnpj(CNPJ)
    
        if store == None or store.senha != Senha:
            return HTTPLoginResponses.STORE_NOT_FOUND()
        else: 
            return HTTPLoginResponses.LOGIN_SUCCESSFUL()
        

    @staticmethod
    def retrieve_password(dados:DadosRetrieveLoja, database = db) -> HttpResponseModel:
        CNPJ = dados.cnpj
        Email = dados.email
        New_password = dados.nsenha

        store = database.get_store_by_cnpj(CNPJ)

        if store == None:
            return HTTPLoginResponses.STORE_NOT_FOUND_UPDATE()
        
        elif Email != store.email:
            return HTTPUpdateStoreResponses.UNAUTORIZED()
        
        else:
            store.update_password({'senha': New_password})
            database.write_to_file()
            return HTTPUpdateStoreResponses.UPDATE_SUCCESS()
        

    @staticmethod
    def change_user_data(dados: DadosChangeLoja, database = db) -> HttpResponseModel:
        CNPJ = dados.cnpj
        Senha = dados.senha
        nSenha = dados.nsenha
        nEmail = dados.nemail
        nCategoria = dados.ncategoria
        nNome = dados.nnome
        
        store = database.get_store_by_cnpj(CNPJ)
        something_changed = False

        if store == None:
            return HTTPLoginResponses.STORE_NOT_FOUND()
        if store.senha != Senha:
            return HTTPUpdateStoreResponses.UNAUTORIZED()
        
        if nSenha and store.senha != nSenha:
            store.update_password({'senha': nSenha})
            something_changed = True
        if nEmail and store.email != nEmail:
            store.update_email({'email': nEmail})
            something_changed = True
        if nNome and store.nome != nNome:
            store.update_nome({'nome': nNome})
            something_changed = True
        if nCategoria and store.categoria != nCategoria:
            store.update_categoria({'categoria': nCategoria})
            something_changed = True

        if something_changed:
            database.write_to_file()
            return HTTPUpdateStoreResponses.UPDATE_SUCCESS()
            
        

