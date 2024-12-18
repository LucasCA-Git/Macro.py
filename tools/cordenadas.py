import pyautogui

def capturar_coordenadas():
    print("Posicione o mouse sobre o ponto desejado e pressione 'Ctrl+C' para capturar.")
    while True:
        try:
            x, y = pyautogui.position()  # Obtém as coordenadas do mouse
            print(f"Coordenadas atuais do mouse: ({x}, {y})")
            pyautogui.sleep(1)
        except KeyboardInterrupt:
            print("Captura de coordenadas interrompida.")
            break

if __name__ == "__main__":
    capturar_coordenadas()
