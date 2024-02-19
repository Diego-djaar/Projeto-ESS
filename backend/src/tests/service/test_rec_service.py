from src.db.__init__ import user_database_example as db
from src.db.__init__ import recuperacao_database_test as db_recuperacao
from src.db.codigos_rec_database import Recuperacao
from src.service.impl.recuperation_service import RecuperationService
from datetime import datetime, timedelta
import pytest
import src.service.impl.signup_service as signup

@pytest.fixture(scope="module")
def user_valido():
    dados_cadastrais = signup.DadosCadastrais(
        username="Peterson", 
        nome = "Peterson", 
        sobrenome="Melo", 
        cpf="111.111.111-02", 
        data_de_nascimento=datetime(2003,5,29), 
        email="Peterson@gmail.com", 
        senha="faculdade123", 
        endereço= "Rua tal", 
        CEP="50000-000"
    )
    
    signup.SingUpService.signup_user(dados_cadastrais, db)

    user = db.get_user_by_email("Peterson@gmail.com")

    yield user

    db.clear_database()
    db_recuperacao.clear_database()

# Fixture para fornecer um email válido para os testes
@pytest.fixture
def email_valido(user_valido):
    return user_valido.email

# Fixture para fornecer um código válido para os testes
@pytest.fixture
def codigo_valido():
    codigo = db_recuperacao.get_rec_by_email("Peterson@gmail.com").codigo
    return codigo

@pytest.fixture
def codigo_expirado(codigo_valido):
    recuperacao = Recuperacao("Peterson@gmail.com",codigo_valido,datetime.now() - timedelta(hours=1,seconds=1) )
    db_recuperacao.add_recuperacao(recuperacao)
    return recuperacao.codigo

# Fixture para fornecer uma nova senha válida para os testes
@pytest.fixture
def nova_senha_valida():
    return "nova_senha123"


# Testes de Recuperação de Conta
def test_recuperar_conta_email_nao_cadastrado():
    assert RecuperationService.recuperar_conta("emailnaocadastrado@example.com", "123456", "nova_senha", "nova_senha", db_user=db, db_recuperacao=db_recuperacao) == "Email não cadastrado"

def test_recuperar_conta_sem_recuperacao(email_valido):
    assert RecuperationService.recuperar_conta(email_valido, "123456", "nova_senha", "nova_senha", db_user=db, db_recuperacao=db_recuperacao) == "Não há recuperação solicitada para este email"

# Testes de Envio de Email
def test_enviar_email(email_valido):
    assert RecuperationService.enviar_email(email_valido, db_user=db, db_recuperacao=db_recuperacao) == True

def test_recuperar_conta(email_valido, codigo_valido, nova_senha_valida):
    assert RecuperationService.recuperar_conta(email_valido, codigo_valido, nova_senha_valida, nova_senha_valida, db_user=db, db_recuperacao=db_recuperacao) == True    

def test_recuperar_conta_codigo_incorreto(email_valido, codigo_valido, nova_senha_valida):
    assert RecuperationService.recuperar_conta(email_valido, "codigo_incorreto", nova_senha_valida, nova_senha_valida, db_user=db, db_recuperacao=db_recuperacao) == "Código Incorreto"

def test_recuperar_conta_senhas_nao_coincidem(email_valido, codigo_valido):
    assert RecuperationService.recuperar_conta(email_valido, codigo_valido, "nova_senha", "outra_senha", db_user=db, db_recuperacao=db_recuperacao) == "Senhas não coincidem"

def test_recuperar_conta_senha_invalida(email_valido, codigo_valido):
    assert RecuperationService.recuperar_conta(email_valido, codigo_valido, "", "", db_user=db, db_recuperacao=db_recuperacao) == "Senha inválida"

def test_recuperar_conta_tempo_expirado(email_valido, codigo_expirado, nova_senha_valida):
    assert RecuperationService.recuperar_conta(email_valido, codigo_expirado, nova_senha_valida, nova_senha_valida, db_user=db, db_recuperacao=db_recuperacao) == "Tempo expirado"
