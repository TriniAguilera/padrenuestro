import typing
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtMultimedia
# import parametros as p

class Luigi(QObject):

    def __init__(self, fila_inicial, columna_inicial):
        super().__init__()
        self.direccion = "R"
        ### la fila inicial y posicion inicial no es propertie porque los limites los controlo en
        ### el constructor.
        self.fila_inicial = fila_inicial
        self.columna_inicial = columna_inicial
        self.posicion_x_inicial = 372 + 53 * columna_inicial + columna_inicial
        self.posicion_y_inicial = 21 + 53 * fila_inicial
        self._fila = fila_inicial
        self._columna = columna_inicial

    @property
    def fila(self):
        return self._fila
    
    @fila.setter
    def fila(self, k):
        if k > 14:
            self._fila = 14
        elif k < 1:
            self._fila = 1
        else:
            self._fila = k

    @property
    def columna(self):
        return self._columna
    
    @columna.setter
    def columna(self, k):
        if k > 9:
            self._columna = 9
        elif k < 1:
            self._columna = 1
        else:
            self._columna = k

    def posicion_X(self):
        return 372 + 53 * self.columna + self.columna
    
    def posicion_Y(self):
        return 21 + 53 * self.fila
    
    def cambiar_direccion(self, nueva_direccion):
        if nueva_direccion.upper() in "URDL":
            self.direccion = nueva_direccion

    def avanzar(self):
        posicion_antigua = (self.posicion_X(), self.posicion_Y())
        suma_fila = 0
        suma_columna = 0
        if self.direccion == "R": ### derecha
            self.columna += 1
            suma_columna += 1
        elif self.direccion == "L": ### izquierda
            self.columna -= 1
            suma_columna -= 1
        elif self.direccion == "U": ### arriba
            self.fila -= 1
            suma_fila -= 1
        elif self.direccion == "D": ### abajo
            self.fila += 1
            suma_fila += 1
        tupla = (posicion_antigua[0] + 26 * suma_columna, posicion_antigua[1] + 26 * suma_fila)
        return self.direccion, (self.fila, self.columna), posicion_antigua, tupla
    
    def obtener_direccion(self):
        return self.direccion
        
class Roca(QObject):

    def __init__(self, fila_inicial, columna_inicial, identificador):
        super().__init__()
        self.direccion = "R"
        self.identificador = identificador
        self.fila_inicial = fila_inicial
        self.columna_inicial = columna_inicial
        self.posicion_x_inicial = 372 + 53 * columna_inicial + columna_inicial
        self.posicion_y_inicial = 21 + 53 * fila_inicial
        self._fila = fila_inicial
        self._columna = columna_inicial

    @property
    def fila(self):
        return self._fila
    
    @fila.setter
    def fila(self, k):
        if k > 14:
            self._fila = 14
        elif k < 1:
            self._fila = 1
        else:
            self._fila = k

    @property
    def columna(self):
        return self._columna
    
    @columna.setter
    def columna(self, k):
        if k > 9:
            self._columna = 9
        elif k < 1:
            self._columna = 1
        else:
            self._columna = k

    def posicion_X(self):
        return 372 + 53 * self.columna + self.columna
    
    def posicion_Y(self):
        return 21 + 53 * self.fila
    
    def cambiar_direccion(self, nueva_direccion):
        if nueva_direccion.upper() in "URDL":
            self.direccion = nueva_direccion

    def avanzar(self):
        posicion_antigua = (self.posicion_X(), self.posicion_Y())
        if self.direccion == "R": ### derecha
            self.columna += 1
        elif self.direccion == "L": ### izquierda
            self.columna -= 1
        elif self.direccion == "U": ### arriba
            self.fila -= 1
        elif self.direccion == "D": ### abajo
            self.fila += 1
        return (self.fila, self.columna), posicion_antigua
    
    def obtener_direccion(self):
        return self.direccion
    
class FantasmaHorizontal(QObject):

    def __init__(self, fila_inicial, columna_inicial, identificador):
        super().__init__()
        self.identificador = identificador
        self.direccion = 1 ##### 1 a derecha y -1 a izquierda
        self.fila_inicial = fila_inicial
        self.columna_inicial = columna_inicial
        self.posicion_x_inicial = 372 + 53 * columna_inicial + columna_inicial
        self.posicion_y_inicial = 21 + 53 * fila_inicial
        self._fila = fila_inicial
        self._columna = columna_inicial

    @property
    def fila(self):
        return self._fila
    
    @fila.setter
    def fila(self, k):
        if k > 14:
            self._fila = 14
        elif k < 1:
            self._fila = 1
        else:
            self._fila = k

    @property
    def columna(self):
        return self._columna
    
    @columna.setter
    def columna(self, k):
        if k > 9:
            self._columna = 9
            self.direccion = -1
        elif k < 1:
            self._columna = 1
            self.direccion = 1
        else:
            self._columna = k

    def posicion_X(self):
        return 372 + 53 * self.columna + self.columna
    
    def posicion_Y(self):
        return 21 + 53 * self.fila

    def avanzar(self):
        posicion_antigua = (self.posicion_X(), self.posicion_Y())
        suma_fila = 0
        suma_columna = 0
        if self.direccion == 1: ### derecha
            self.columna += 1
            suma_columna += 1
        elif self.direccion == -1: ### izquierda
            self.columna -= 1
            suma_columna -= 1
        tupla = (posicion_antigua[0] + 26 * suma_columna, posicion_antigua[1] + 26 * suma_fila)
        return self.direccion, (self.fila, self.columna), posicion_antigua, tupla
    
    def obtener_direccion(self):
        return self.direccion
    
class FantasmaVertical(QObject):

    def __init__(self, fila_inicial, columna_inicial, identificador):
        super().__init__()
        self.identificador = identificador
        self.direccion = 1 ##### 1 a arriba y -1 a abajo
        self.fila_inicial = fila_inicial
        self.columna_inicial = columna_inicial
        self.posicion_x_inicial = 372 + 53 * columna_inicial + columna_inicial
        self.posicion_y_inicial = 21 + 53 * fila_inicial
        self._fila = fila_inicial
        self._columna = columna_inicial

    @property
    def fila(self):
        return self._fila
    
    @fila.setter
    def fila(self, k):
        if k > 14:
            self._fila = 14
            self.direccion = 1
        elif k < 1:
            self._fila = 1
            self.direccion = -1
        else:
            self._fila = k

    @property
    def columna(self):
        return self._columna
    
    @columna.setter
    def columna(self, k):
        if k > 9:
            self._columna = 9
        elif k < 1:
            self._columna = 1
        else:
            self._columna = k

    def posicion_X(self):
        return 372 + 53 * self.columna + self.columna
    
    def posicion_Y(self):
        return 21 + 53 * self.fila

    def avanzar(self):
        posicion_antigua = (self.posicion_X(), self.posicion_Y())
        suma_fila = 0
        suma_columna = 0
        if self.direccion == 1: ### arriba
            self.fila -= 1
            suma_fila -= 1
        elif self.direccion == -1: ### abajo
            self.fila += 1
            suma_fila += 1
        tupla = (posicion_antigua[0] + 26 * suma_columna, posicion_antigua[1] + 26 * suma_fila)
        return self.direccion, (self.fila, self.columna), posicion_antigua, tupla
    
    def obtener_direccion(self):
        return self.direccion

class Musica(QObject):

    def __init__(self, ruta_cancion):
        super().__init__()
        self.ruta_cancion = ruta_cancion

    def comenzar(self):
        self.cancion = QtMultimedia.QSound(self.ruta_cancion)
        self.cancion.setLoops(2147483647)
        self.cancion.play()
        print("Comienza musica")

    def pausar(self):
        self.cancion.stop()