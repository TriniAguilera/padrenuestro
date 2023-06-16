from PyQt5.QtCore import QObject, pyqtSignal
from backend.clases_objetos import Musica
import parametros as p

class LogicaDerrota(QObject):
    
    senal_iniciar_juego = pyqtSignal(str, str) ## conecto con definir nombre de logica

    def __init__(self):
        super().__init__()
        # self.musica = Musica(p.RUTA_MUSICA_DERROTA)

    def definir_nombre(self, nombre, archivo, booleano):
        self.nombre = nombre
        self.archivo = archivo
        # if booleano:
        #     self.musica = Musica(p.RUTA_MUSICA_VICTORIA)
        # else:
        #     self.musica = Musica(p.RUTA_MUSICA_DERROTA)

    def volver_jugar(self):
        self.senal_iniciar_juego.emit(self.nombre, self.archivo)

    def stop_musica(self):
        self.musica.pausar()

    def comenzar_musica(self):
        self.musica.comenzar()