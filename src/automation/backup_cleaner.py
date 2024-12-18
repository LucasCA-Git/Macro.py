import os
import shutil
import tkinter as tk
from tkinter import filedialog
import logging

# Configuração do log
log_file = 'logs/bckpCleaner.log'

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Função para escolher o diretório
def escolher_diretorio(title="Escolha uma pasta"):
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    pasta = filedialog.askdirectory(title=title)
    return pasta

# Função para fazer o backup
def fazer_backup(origem, destino):
    try:
        # Verifica se o diretório de origem existe
        if not os.path.exists(origem):
            logging.error(f"O diretório de origem '{origem}' não existe.")
            return False
        
        # Verifica se o diretório de destino existe, cria se não
        if not os.path.exists(destino):
            os.makedirs(destino)

        # Copia os arquivos da origem para o destino
        for item in os.listdir(origem):
            origem_item = os.path.join(origem, item)
            destino_item = os.path.join(destino, item)

            try:
                if os.path.isdir(origem_item):
                    shutil.copytree(origem_item, destino_item)
                    logging.info(f"Diretório '{origem_item}' copiado para '{destino_item}'.")
                else:
                    shutil.copy2(origem_item, destino_item)
                    logging.info(f"Arquivo '{origem_item}' copiado para '{destino_item}'.")
            except Exception as e:
                logging.error(f"Erro ao copiar '{origem_item}': {e}")
                return False

        logging.info(f"Backup de '{origem}' para '{destino}' concluído com sucesso.")
        return True

    except Exception as e:
        logging.error(f"Erro ao realizar o backup: {e}")
        return False

if __name__ == "__main__":
    # Escolher a pasta de origem
    pasta_origem = escolher_diretorio("Escolha a pasta para fazer o backup")
    if not pasta_origem:
        logging.warning("Nenhuma pasta de origem selecionada.")
        exit()

    # Escolher a pasta de destino
    pasta_destino = escolher_diretorio("Escolha o local de destino para o backup")
    if not pasta_destino:
        logging.warning("Nenhuma pasta de destino selecionada.")
        exit()

    # Realizar o backup
    sucesso = fazer_backup(pasta_origem, pasta_destino)

    if sucesso:
        logging.info("Processo de backup completo.")
    else:
        logging.error("O backup falhou.")
