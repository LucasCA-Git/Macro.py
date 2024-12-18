import os
import subprocess
import logging
import time

# Configuração do log
log_file = 'logs/installBasics.log'

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename=log_file,  
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s',  
)

# Função para verificar se o programa está instalado
def is_installed(program_name):
    try:
        result = subprocess.run([program_name, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except FileNotFoundError:
        return False

# Função para instalar o programa usando o Chocolatey (caso não esteja instalado)
def install_choco_package(package_name):
    try:
        logging.info(f"Iniciando instalação do {package_name}...")
        subprocess.run(["choco", "install", package_name, "-y"], check=True)
        logging.info(f"{package_name} instalado com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao instalar {package_name}: {e}")
        logging.warning(f"Falha na instalação de {package_name}. Tentando novamente...")
        time.sleep(5)
        subprocess.run(["choco", "install", package_name, "-y"], check=True)

def install_basics():
    # Google Chrome
    if not is_installed("chrome"):
        install_choco_package("googlechrome")
    else:
        logging.info("Google Chrome já está instalado.")

    # 7-Zip
    if not is_installed("7z"):
        install_choco_package("7zip")
    else:
        logging.info("7-Zip já está instalado.")

    # Notepad++
    if not is_installed("notepad++"):
        install_choco_package("notepadplusplus.install")
    else:
        logging.info("Notepad++ já está instalado.")

    # Visual Studio Code
    if not is_installed("code"):
        install_choco_package("vscode")
    else:
        logging.info("Visual Studio Code já está instalado.")

    # Java JDK
    if not is_installed("java"):
        install_choco_package("adoptopenjdk")
    else:
        logging.info("Java JDK já está instalado.")

    # Python
    if not is_installed("python"):
        install_choco_package("python")
    else:
        logging.info("Python já está instalado.")

    # Node.js
    if not is_installed("node"):
        install_choco_package("nodejs")
    else:
        logging.info("Node.js já está instalado.")

if __name__ == "__main__":
    install_basics()
