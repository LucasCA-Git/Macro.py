import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Carregar as variáveis do .env
load_dotenv()

# Configuração de e-mail e senha no .env
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Configuração de logging
logging.basicConfig(
    filename="logs/emailService.log",  # Caminho do log
    level=logging.INFO,  # Nível de log
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato do log
)

def send_email(subject, body, recipient):
    """Envia um e-mail com o corpo especificado."""
    try:
        # Criar a mensagem
        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Conectar ao servidor de SMTP e enviar o e-mail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Iniciar o TLS (segurança)
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        logging.info(f"E-mail enviado para {recipient} com assunto '{subject}'.")
        print(f"E-mail enviado para {recipient}")

    except Exception as e:
        logging.error(f"Erro ao enviar e-mail para {recipient}: {e}")
        print(f"Erro ao enviar e-mail: {e}")

# Exemplo de uso
if __name__ == "__main__":
    recipient = "destinatario@example.com"  # Alterar para o destinatário real
    subject = "Assunto do e-mail"
    body = "Corpo do e-mail com informações relevantes."
    send_email(subject, body, recipient)
