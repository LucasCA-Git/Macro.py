# Automation Helper
[![GitHub](https://img.shields.io/github/license/LucasCA-Git/automation-helper)](https://github.com/LucasCA-Git/automation-helper)  
[![GitHub issues](https://img.shields.io/github/issues/LucasCA-Git/automation-helper)](https://github.com/LucasCA-Git/automation-helper/issues)  
[![GitHub stars](https://img.shields.io/github/stars/LucasCA-Git/automation-helper?style=social)](https://github.com/LucasCA-Git/automation-helper/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/LucasCA-Git/automation-helper?style=social)](https://github.com/LucasCA-Git/automation-helper/network)

O **Automation Helper** é uma ferramenta para automatizar várias tarefas no Windows. Ele inclui funcionalidades como:

- Limpeza de arquivos temporários
- Backup de arquivos
- Envio de logs por e-mail
- Instalação de programas essenciais
- Ferramentas bônus como verificação de coordenadas do mouse e abas abertas no Windows

Este projeto foi desenvolvido para facilitar a automação de tarefas rotineiras, melhorar a produtividade e a manutenção do sistema.


## Tecnologias Usadas

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)  
![NPM](https://img.shields.io/badge/NPM-7.0%2B-yellow?logo=npm&logoColor=white)  
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-%20-%2300BFFF?logo=python&logoColor=white)  
![PyGetWindow](https://img.shields.io/badge/PyGetWindow-%20-%231f3d5e?logo=python&logoColor=white)  
![Pynput](https://img.shields.io/badge/Pynput-%20-%2300B0D0?logo=python&logoColor=white)  
![Python-Dotenv](https://img.shields.io/badge/Python%20Dotenv-%20-%23009a8e?logo=python&logoColor=white)  

### 1. **Limpeza de Arquivos Temporários** (`clear_temp.py`)

Este script remove arquivos temporários do sistema para liberar espaço e melhorar o desempenho do computador. Ele pode ser executado de forma simples, limpando pastas como a `Temp` do Windows.

### Como utilizar:

Execute o comando:

```bash  
npm run clear-temp  
```  
2. Backup de Arquivos (backup_cleaner.py)  
Este script permite fazer backup de arquivos de um diretório para outro. Após a cópia dos arquivos, o diretório de origem é limpo.

Como usar:  
Execute o comando:

```bash  
npm run clean-backup  
```  

### 3. Envio de Logs por E-mail (email_service.py)  
- Este script envia logs de execução de qualquer automação para um e-mail pré-configurado. Isso é útil para acompanhar a execução dos processos, especialmente para tarefas programadas ou em segundo plano.

Como usar:  
Execute o comando:

```bash  
npm run send-logs  
```  
### 4. Instalação de Programas Essenciais (install_basics.py)  
- Este script realiza a instalação de programas básicos como o Google Chrome, caso não estejam instalados no sistema. Ele é projetado para ser utilizado em novos computadores ou após formatação.

Como usar:  
Execute o comando:

```bash  
npm run install  
```  

## Requisitos  
- Python 3.9 ou superior  
 
- Bibliotecas Python: pygetwindow, pyautogui, pywin32, pynput, python-dotenv  
Node.js e NPM para executar os scripts JavaScript  
Dependências  
Python Packages:  
pygetwindow  
pyautogui  
pywin32  
pynput  
python-dotenv  
Node.js Packages:  
npm  
Licença  
Este projeto está licenciado sob a MIT License.  


