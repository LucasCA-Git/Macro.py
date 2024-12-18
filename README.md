# Automation Helper

<p align="center">
  <a href="https://github.com/LucasCA-Git/automation-helper">
    <img src="https://img.shields.io/github/license/LucasCA-Git/automation-helper" alt="License">
  </a>
  <a href="https://github.com/LucasCA-Git/automation-helper/issues">
    <img src="https://img.shields.io/github/issues/LucasCA-Git/automation-helper" alt="Issues">
  </a>
  <a href="https://github.com/LucasCA-Git/automation-helper/stargazers">
    <img src="https://img.shields.io/github/stars/LucasCA-Git/automation-helper?style=social" alt="Stars">
  </a>
  <a href="https://github.com/LucasCA-Git/automation-helper/network">
    <img src="https://img.shields.io/github/forks/LucasCA-Git/automation-helper?style=social" alt="Forks">
  </a>
</p>

O **Automation Helper** é uma ferramenta para automatizar várias tarefas no Windows. Ele inclui funcionalidades como:

- Conversação em chat
- Limpeza de arquivos temporários
- Backup de arquivos
- Envio de logs por e-mail
- Instalação de programas essenciais
- Ferramentas bônus como verificação de coordenadas do mouse e abas abertas no Windows

Este projeto foi desenvolvido para facilitar a automação de tarefas rotineiras, melhorar a produtividade e a manutenção do sistema.

# Projeto de Automação com Python

## Linguagem Utilizada

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white" alt="Python">  
</p>

## **Bibliotecas Utilizadas**

<p align="center">
  <img src="https://img.shields.io/badge/PyAutoGUI-%20-%2300BFFF?logo=python&logoColor=white" alt="PyAutoGUI">  
  <img src="https://img.shields.io/badge/PyGetWindow-%20-%231f3d5e?logo=python&logoColor=white" alt="PyGetWindow">  
  <img src="https://img.shields.io/badge/Pynput-%20-%2300B0D0?logo=python&logoColor=white" alt="Pynput">  
  <img src="https://img.shields.io/badge/PyWin32-%20-%23009a8e?logo=python&logoColor=white" alt="PyWin32">  
  <img src="https://img.shields.io/badge/NPM-%20-%23000000?logo=npm&logoColor=white" alt="NPM">  
  <img src="https://img.shields.io/badge/Python%20Dotenv-%20-%23009a8e?logo=python&logoColor=white" alt="Python-Dotenv">  
  <img src="https://img.shields.io/badge/NLTK-%20-%23000f00?logo=nltk&logoColor=white" alt="NLTK">  
  <img src="https://img.shields.io/badge/OpenAI-%20-%2300BFFF?logo=openai&logoColor=white" alt="OpenAI">  
</p>

## Funcionalidades

### 1. **Limpeza de Arquivos Temporários** (`clear_temp.py`)

Este script remove arquivos temporários do sistema para liberar espaço e melhorar o desempenho do computador. Ele pode ser executado de forma simples, limpando pastas como a `Temp` do Windows.

### Como utilizar:

Execute o comando:

```bash  
python src/automation/clear_temp.py
```
### 2. Backup de Arquivos (backup_cleaner.py)
Este script permite fazer backup de arquivos de um diretório para outro. Após a cópia dos arquivos, o diretório de origem é limpo.

### Como utilizar:

Execute o comando:
```bash  
python src/automation/backup_cleaner.py
```
### 3. Envio de Logs por E-mail (email_service.py)
Este script envia logs de execução de qualquer automação para um e-mail pré-configurado. Isso é útil para acompanhar a execução dos processos, especialmente para tarefas programadas ou em segundo plano.

### Como utilizar:

Execute o comando:
```bash  
python src/automation/email_service.py
```

### 4. Instalação de Programas Essenciais (install_basics.py)
Este script realiza a instalação de programas básicos como o Google Chrome, caso não estejam instalados no sistema. Ele é projetado para ser utilizado em novos computadores ou após formatação.

### Como utilizar:
Execute o comando:
```bash  
python src/automation/install_basics.py
```

# Como Conversar com o Chatbot
Você pode interagir com o chatbot para realizar as automações de maneira mais simples e intuitiva. O chatbot ajudará a executar tarefas como:

- Limpar arquivos temporários
- Fazer backup de arquivos
- Enviar logs por e-mail
- Instalar programas essenciais
## Para iniciar o chatbot, siga os passos abaixo:

Execute o comando para iniciar o chatbot:
```bash  
python src/automation/chatbot.py
```

O chatbot irá responder com opções de comandos. Você pode interagir digitando as opções conforme necessário. 

- Quando você digitar "sair", a conversa será encerrada.

## Explicação Técnica

#### **Bibliotecas Utilizadas**


- **PyAutoGUI**: Automação de interações de GUI, como controle de mouse e teclado.
- **PyGetWindow**: Manipulação de janelas abertas no Windows.
- **Pynput**: Monitoramento e controle de teclado e mouse para automatizar entradas.
- **Python Dotenv**: Carrega variáveis de ambiente de arquivos `.env`, melhorando a segurança e flexibilidade de configurações.
- **PyWin32**: Conjunto de bibliotecas para interagir com APIs do Windows.
- **NPM**: Gerenciador de pacotes para JavaScript, usado para instalações e dependências de front-end.
- **Python-Dotenv**: Utilizado para carregar variáveis de ambiente de arquivos `.env`.
- **NLTK**: Biblioteca para processamento de linguagem natural, utilizada principalmente para análise de texto.
- **OpenAI**: OpenAi para o chatbot via console

#### **Chatbot**
O chatbot permite interação natural com o sistema de automação, oferecendo uma interface simples para realizar tarefas automatizadas sem memorizar comandos técnicos.

### Arquitetura do Código

A estrutura modular organiza os scripts em `src/automation/`, com cada script responsável por uma tarefa específica, como limpar arquivos temporários, fazer backup, enviar e-mails ou instalar programas essenciais.

### Interação entre os Scripts

- **clear_temp.py**: Remove arquivos temporários.
- **backup_cleaner.py**: Faz backup e limpa diretórios.
- **email_service.py**: Envia logs por e-mail.
- **install_basics.py**: Instala programas essenciais no sistema.

---
# Documentação da Pasta "logs"

A pasta **logs** é um componente fundamental do projeto, destinada a armazenar registros detalhados das operações e execuções dos scripts, incluindo interações com o chatbot e atividades de automação. Os arquivos de log gerados nesta pasta desempenham um papel crucial na depuração, monitoramento e verificação de erros, fornecendo informações vitais sobre o funcionamento do sistema.

## Estrutura da Pasta

A pasta **logs** contém arquivos que são constantemente atualizados durante a execução dos scripts e do chatbot. Cada script ou ferramenta que gera logs terá um arquivo correspondente que armazena informações sobre suas execuções, incluindo mensagens de erro, sucesso e outros eventos importantes.

### Arquivos de Log Comuns

- **chatbot.log**: Registra as interações do usuário com o chatbot, incluindo os comandos executados e as respostas fornecidas. Ajuda a rastrear as atividades do chatbot e identificar falhas ou erros nas interações.
  
- **clear_temp.log**: Armazena logs detalhados da execução do script `clear_temp.py`, que é responsável por limpar arquivos temporários do sistema. Este arquivo pode incluir informações sobre o sucesso ou falha do processo e mensagens de erro relacionadas à remoção de arquivos.

- **backup_cleaner.log**: Registra informações sobre a execução do script `backup_cleaner.py`, que realiza a tarefa de backup de arquivos e limpeza de diretórios. Logs podem incluir detalhes sobre os arquivos copiados e erros ocorridos durante a execução.

- **email_service.log**: Armazena logs do script `email_service.py`, que envia emails com os logs de execução. Ele pode registrar informações sobre o sucesso ou falha ao tentar enviar os emails, bem como mensagens de erro relacionadas ao processo de envio.

- **install_basics.log**: Contém logs da execução do script `install_basics.py`, responsável pela instalação de programas essenciais. O arquivo registra detalhes sobre os programas instalados, falhas de instalação e qualquer outro evento relevante durante o processo.

## Como a Pasta "logs" Ajuda na Verificação de Erros

A pasta **logs** desempenha um papel fundamental na identificação e correção de erros no sistema. Veja como ela auxilia no processo:

### 1. **Rastreamento de Execução dos Scripts**
Cada script gera um log detalhado das suas ações. Isso é útil para entender exatamente o que ocorreu durante a execução e identificar onde um erro pode ter ocorrido. Por exemplo, se o script de backup falhar, o log indicará exatamente qual etapa do processo não foi concluída com sucesso, como problemas ao acessar diretórios ou permissões.

### 2. **Identificação de Erros e Falhas**
Sempre que um erro ocorre em qualquer script, ele é registrado no arquivo de log correspondente. Mensagens de erro detalhadas fornecem informações sobre a causa do problema, como exceções de Python ou falhas na execução de comandos. Isso ajuda os desenvolvedores a identificar e corrigir rapidamente qualquer falha que ocorra.

### 3. **Monitoramento de Comandos Executados**
Os logs ajudam a monitorar quais comandos foram executados e quando, além de fornecer o status de cada operação (sucesso ou falha). No caso do chatbot, o log pode indicar quais comandos o usuário solicitou, se o script foi executado corretamente ou se houve algum problema.

### 4. **Análise de Desempenho**
Através dos logs, é possível analisar o desempenho de cada script. Por exemplo, quanto tempo um processo de backup levou para ser concluído ou se algum script demorou mais do que o esperado para ser executado. Isso pode ajudar na otimização de processos e na melhoria da eficiência do sistema.

### 5. **Facilidade na Depuração**
Ao tentar depurar um erro, os logs fornecem uma trilha detalhada dos eventos que ocorreram antes do erro. Com essas informações, é mais fácil reproduzir o problema e testar soluções, sem a necessidade de revisar manualmente todo o processo de execução.


Aqui está um exemplo de final para a licença em markdown:

markdown
Copiar código
## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

A licença MIT é uma licença permissiva que permite que você faça quase qualquer coisa com o código, incluindo usá-lo, modificá-lo, distribuí-lo e sublicenciá-lo, desde que inclua o aviso de copyright e a renúncia de responsabilidade. Não há garantia de nenhum tipo sobre o código fornecido.
