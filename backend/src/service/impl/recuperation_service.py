from src.db.__init__ import user_database as db_user
from src.db.__init__ import recuperacao_database as db_recuperacao
from src.db.codigos_rec_database import Recuperacao
import random, string, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

class RecuperationService:
    @staticmethod
    def enviar_email(email :str):

        if not db_user.get_user_by_email(email):
            return False

        codigo = ''.join(random.choices(string.digits, k=6))

        recuperacao = Recuperacao(email, codigo)
        db_recuperacao.add_recuperacao(recuperacao)

        email_remetente = "emailprojetoess@gmail.com"
        senha_email_remetente = "yayv sgbc urzy frua"

        # Criação do objeto MIMEMultipart
        msg = MIMEMultipart()
        msg['From'] = email_remetente
        msg['To'] = email
        msg['Subject'] = "Código de recuperação"
        
        # Adicionando o corpo do e-mail
        msg.attach(MIMEText(codigo, 'plain'))
        
        # Inicializando a conexão com o servidor SMTP do Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Faça login no servidor SMTP do Gmail
        server.login(email_remetente, senha_email_remetente)
        
        # Enviando o e-mail
        texto = msg.as_string()
        server.sendmail(email_remetente, email, texto)
        
        # Fechando a conexão com o servidor SMTP do Gmail
        server.quit()

    @staticmethod
    def recuperar_conta(email: str, codigo: str, nova_senha: str, nova_senha_repetida: str):

        user = db_user.get_user_by_email(email)
        recuperacao = db_recuperacao.get_rec_by_email(email)
        
        if not user:
            return "Email não cadastrado"

        if not recuperacao:
            return "Não há recuperação solicitada para este email"
        
        if recuperacao.codigo != codigo:
            return "Código Incorreto"
        
        if nova_senha != nova_senha_repetida:
            return "Senhas não coicidem"
        
        if not db_user.valid_password(nova_senha):
            return "Senha inválida"
        
        if datetime.now() - recuperacao.date > timedelta(hours=1):
            return "Tempo inspirado"
        
        user.add_password(nova_senha)
        db_user.write_to_file()
        return True