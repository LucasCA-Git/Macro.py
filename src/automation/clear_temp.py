import os
import shutil
import tempfile
import logging

# Configuração do logging
log_file = 'logs/clearTemp.log'

# Criar o diretório de logs se não existir
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename=log_file,  # Nome do arquivo de log
    level=logging.INFO,  # Nível de log
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato da mensagem no log
)

def clear_temp():
    temp_dir = tempfile.gettempdir()  # Obtém o diretório temporário
    logging.info(f"Limpeza do diretório temporário: {temp_dir}")

    try:
        # Exclui todos os arquivos no diretório temp
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            try:
                # Se for um arquivo, exclui
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    logging.info(f"Arquivo {file_path} excluído.")
                # Se for um diretório, tenta excluir recursivamente
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    logging.info(f"Diretório {file_path} excluído.")
            except PermissionError:
                logging.warning(f"Permissão negada para excluir: {file_path}")
            except Exception as e:
                logging.error(f"Erro ao excluir {file_path}: {e}")
    except Exception as e:
        logging.error(f"Erro ao acessar o diretório temporário: {e}")

if __name__ == "__main__":
    clear_temp()
