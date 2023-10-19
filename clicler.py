import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

retraso = 0.001
boton = Button.left
tecla_repetir = KeyCode(char='+')  # Tecla para repetir el clic
tecla_salir = KeyCode(char='-')

class ClickMouse(threading.Thread):
    def __init__(self, retraso, boton):
        super(ClickMouse, self).__init__()
        self.retraso = retraso
        self.boton = boton
        self.repetir = False
        self.programa_ejecutandose = True

    def alternar_repetir(self):
        self.repetir = not self.repetir

    def salir(self):
        self.programa_ejecutandose = False

    def run(self):
        while self.programa_ejecutandose:
            if self.repetir:
                mouse.click(self.boton)
                time.sleep(self.retraso)
            else:
                time.sleep(0.1)

mouse = Controller()
hilo_clic = ClickMouse(retraso, boton)
hilo_clic.start()

def al_presionar(tecla):
    if tecla == tecla_repetir:
        hilo_clic.alternar_repetir()
    elif tecla == tecla_salir:
        hilo_clic.salir()
        listener.stop()

with Listener(on_press=al_presionar) as listener:
    listener.join()
