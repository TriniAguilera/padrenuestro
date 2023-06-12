from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p

class LogicaInicio(QObject):
    
    senal_respuesta_validacion = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def comprobar_nombre(self, nombre):
        print("Comprobando nombre en logica")
        if nombre.isalnum() and len(nombre) >= p.MIN_CARACTERES and len(nombre) <= p.MAX_CARACTERES:
            self.senal_respuesta_validacion.emit([nombre, True, ""])
            print("Logica, nombre bueno")
        else:
            lista_errores = []
            if not nombre.isalnum():
                lista_errores.append("alfanumerico")
                print("Logica, error alfanumerico")
            if len(nombre) < p.MIN_CARACTERES:
                lista_errores.append("caracter")
                print("Logica, error caracter menor")
            if len(nombre) > p.MAX_CARACTERES:
                lista_errores.append("caracter")
                print("Logica, error caracter mayor")
            self.senal_respuesta_validacion.emit([nombre, False, lista_errores])

    