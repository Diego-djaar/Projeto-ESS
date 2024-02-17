from src.db.__init__ import user_database as db_user
from src.db.__init__ import recuperacao_database as db_recuperacao
from src.db.codigos_rec_database import Recuperacao
import random, string, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

