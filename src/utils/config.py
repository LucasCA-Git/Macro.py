from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações de e-mail
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
