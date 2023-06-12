import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMessageBox
import parametros as p 

window_name, base_class = uic.loadUiType(p.RUTA_VENTANA_INICIO)

class VentanaInicio (window_name, base_class):

    senal_verificar_usuario = pyqtSignal(str)
    senal_iniciar_constructor = pyqtSignal(str)
    senal_iniciar_juego = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_actual = "None"
        self.boton_comenzar.clicked.connect(self.verificar_nombre)
        self.boton_salir.clicked.connect(self.ocultar)

    def verificar_nombre(self):
        print("Verificando nombre")
        self.senal_verificar_usuario.emit(self.edit_usuario.text())

    def recibir_validacion(self, lista_respuesta):
        if lista_respuesta[1]:
            self.hide()
            self.verificar_combo_box(lista_respuesta[0])
        else:
            self.pop_up_error(lista_respuesta)

    def pop_up_error(self, lista_respuesta):
        if "alfanumerico" in lista_respuesta[2] and "caracter" in lista_respuesta[2]:
            QMessageBox.about(self, "ERROR", "El nombre del usuario no es alfanumerico y su largo"\
                                f" no está dentro del rango de caracteres [{p.MIN_CARACTERES},"\
                                f" {p.MAX_CARACTERES}]. \nVuelva a intentarlo.")
            self.edit_usuario.setText("")
        elif lista_respuesta[2] == "None":
            QMessageBox.about(self, "ERROR", "Debes seleccionar un mapa o el modo constructor.")
        else:
            if "alfanumerico" in lista_respuesta[2]:
                QMessageBox.about(self, "ERROR", "El nombre del usuario no es alfanumerico. "\
                                  f"\nVuelva a intentarlo.")
            else:
                QMessageBox.about(self, "ERROR", f"El largo del nombre de usuario no está dentro"\
                    f" del rango [{p.MIN_CARACTERES}, {p.MAX_CARACTERES}]. \nVuelva a intentarlo.")
                self.edit_usuario.setText("")
        

    def verificar_combo_box(self, nombre):
        self.comboBox_actual = str(self.comboBox_inicio.currentText())
        if self.comboBox_actual == "modo constructor":
            self.senal_iniciar_constructor.emit(nombre)
        elif self.comboBox_actual == "None":
            self.pop_up_error(["None", "None", "None"])
        else:
            actual = self.comboBox_actual
            self.senal_iniciar_juego.emit(nombre, actual)

    def ocultar(self):
        self.hide()
        sys.exit()

    def mostrar(self):
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.mostrar()
    sys.exit(app.exec())