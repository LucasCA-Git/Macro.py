import openai
import os
from dotenv import load_dotenv
import json
import subprocess
import logging

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração da chave da API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Função para carregar informações do arquivo JSON
def carregar_informacoes(arquivo):
    if arquivo.endswith('.json'):
        with open(arquivo, 'r') as file:
            return json.load(file)
    else:
        return "Arquivo não suportado!"

# Função para executar o comando
def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        return resultado.stdout if resultado.returncode == 0 else resultado.stderr
    except Exception as e:
        return f"Erro ao executar o comando: {str(e)}"

# Função para gerar a resposta do GPT-4
def gerar_resposta_gpt4(prompt):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Função principal do chatbot
def chatbot():
    # Carregar informações do JSON
    info_chatbot = carregar_informacoes('src/doc/info_automacao.json')  # Ajuste para o caminho do seu arquivo JSON

    # Exibir saudação inicial
    print(info_chatbot['greetings']['welcome'])
    print(info_chatbot['greetings']['options_prompt'])

    # Mostrar opções de comando
    for cmd in info_chatbot['commands']:
        print(f"{cmd['option']} - {cmd['description']}")

    while True:
        usuario_input = input("Você: ").lower()

        # Se o usuário digitar "sair", encerra a conversa
        if usuario_input == 'sair':
            print("Chatbot: Até logo! Volte sempre.")
            break

        # Tratar saudações iniciais
        elif usuario_input in ['oi', 'olá', 'e aí', 'oii', 'olá!']:
            print(info_chatbot['greetings']['welcome'])
            print(info_chatbot['greetings']['options_prompt'])
            for cmd in info_chatbot['commands']:
                print(f"{cmd['option']} - {cmd['description']}")

        # Verificar se a entrada corresponde a um comando
        else:
            try:
                option = int(usuario_input)
                comando = next((cmd for cmd in info_chatbot['commands'] if cmd['option'] == option), None)

                if comando:
                    print(f"Chatbot: Executando: {comando['description']}...")
                    resposta = executar_comando(comando['script'])
                    print(f"Chatbot: {resposta}")
                else:
                    # Se o comando não for encontrado, gerar uma resposta do GPT-4
                    prompt = f"Usuário disse: '{usuario_input}'. Como posso ajudar?"
                    resposta_gpt4 = gerar_resposta_gpt4(prompt)
                    print(f"Chatbot (GPT-4): {resposta_gpt4}")
            except ValueError:
                print("Chatbot: Não entendi a opção. Digite o número da opção ou 'sair' para encerrar.")

if __name__ == "__main__":
    chatbot()
