import pygetwindow as gw

def listar_janelas():
    # Obtém todas as janelas abertas no sistema
    janelas = gw.getAllTitles()
    print("Janelas abertas no sistema:")
    for i, janela in enumerate(janelas):
        if janela:  # Ignora janelas com títulos vazios
            print(f"{i + 1}. {janela}")
    return janelas

# Teste para listar janelas
if __name__ == "__main__":
    listar_janelas()
