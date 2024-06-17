import keyboard

def detectar_tecla(evento):
    with open('teclas_presionadas.txt', 'a') as archivo:
        archivo.write(f"{evento.name}\n")

keyboard.on_press(detectar_tecla)

keyboard.wait('esc')