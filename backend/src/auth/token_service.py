import datetime
from pydantic import BaseModel
from schemas.response import HTTPResponses, HttpResponseModel
from db.user_database import User, UserDatabase
from schemas.user_response import HTTPLoginResponses
from random import randrange
from bidict import bidict



class TokenService():
    # TODO: desativar sessões condicionalmente
    sessoes_ativas = set()
    sessao_usuario = bidict()
    
    def add_user(self, user: User):
        """Assinala a sessão desse usuário como ativa, retornando o token de sessão

        Args:
            user (User): usuário

        Returns:
            (int): token de sessão
        """
        token: int
        while True:
            token = randrange(680564733841877000000000, 1157920892373162000000000000000000)
            if hash(token) not in self.sessoes_ativas:
                self.sessoes_ativas.add(hash(token))
                break
        self.sessao_usuario.forceput(hash(token), user)
        return token
    
    def rm_user(self, token = None, user = None):
        if token == None and user == None:
            return
        if token == None:
            hash_token = self.sessao_usuario.inverse[user]
            self.sessao_usuario.pop(hash_token)
            self.sessoes_ativas.remove(hash_token)
        if user == None:
            self.sessao_usuario.pop(hash(token))
            self.sessoes_ativas.remove(hash(token))
    
    def get_user_of_token(self, token: int) -> User | None:
        return self.sessao_usuario.get(hash(token), None)
    
    def user_active(self, token: int) -> bool:
        return hash(token) in self.sessoes_ativas
    
    def clear(self):
        self.sessoes_ativas.clear()
        self.sessao_usuario.clear()
