import typing
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, Qt, QRect, QPoint, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QMessageBox, QLineEdit, QPushButton, QComboBox, \
    QHBoxLayout, QVBoxLayout, QGridLayout, QApplication)

######### FALTA IMPORTAR PARAMETROS

class VentanaDerrota(QWidget):

    senal_inicio_musica = pyqtSignal() ### conectamos con comenzar musica de logica post
    senal_detener_musica = pyqtSignal()
    senal_volver_jugar = pyqtSignal() ### conectamos con logica derrota

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(100, 100, 1000, 900)
        
        self.label_game_over = QLabel(self)
        self.label_game_over.setGeometry(160, 150, 800, 300)

        self.label_nombre = QLabel('NOMBRE: ', self)
        self.label_nombre.setGeometry(200, 350, 800, 100)
        self.label_nombre.setFont(QFont("calibri", 25))

        self.label_puntaje_total = QLabel("PUNTAJE TOTAL: ", self)
        self.label_puntaje_total.setGeometry(200, 425, 800, 100)
        self.label_puntaje_total.setFont(QFont("calibri", 25))

        self.label_vidas = QLabel('VIDAS: ', self)
        self.label_vidas.setGeometry(200, 500, 800, 100)      
        self.label_vidas.setFont(QFont("calibri", 25))

        self.label_tiempo_restante = QLabel('TIEMPO RESTANTE: ', self)
        self.label_tiempo_restante.setGeometry(200, 575, 800, 100)      
        self.label_tiempo_restante.setFont(QFont("calibri", 25))

        self.boton_salir = QPushButton(self)
        self.boton_salir.setGeometry(QRect(QPoint(275, 700), QSize(200, 50)))
        self.boton_salir.setText("SALIR")
        self.boton_salir.setStyleSheet("background-color: white")
        self.boton_salir.setFont(QFont("calibri", 15))
        self.boton_salir.clicked.connect(self.ocultar)

        self.boton_volver = QPushButton(self)
        self.boton_volver.setGeometry(QRect(QPoint(525, 700), QSize(200, 50)))
        self.boton_volver.setText("VOLVER A JUGAR")
        self.boton_volver.setStyleSheet("background-color: white")
        self.boton_volver.setFont(QFont("calibri", 15))
        self.boton_volver.clicked.connect(self.volver)

    def volver(self):
        self.hide()
        # self.senal_detener_musica.emit()
        self.senal_volver_jugar.emit()

    def mostrar(self, tiempo, vidas, puntaje, nombre, resultado):
        # tiempo restante, vidas, puntaje, nombre de usuario, gana/pierde
        # self.senal_inicio_musica.emit()

        if not resultado:
            self.setStyleSheet("background-color: red")
            self.setWindowTitle("Ventana Derrota")
            self.label_game_over.setText("¡GAME OVER!")
        else:
            self.setStyleSheet("background-color: rgb(85, 255, 0)")
            self.setWindowTitle("Ventana Victoria")
            self.label_game_over.setText("¡GANASTE!")
        self.label_game_over.setFont(QFont("calibri", 80))

        self.label_tiempo_restante.setText(f"TIEMPO RESTANTE: {tiempo} segundos")
        self.label_vidas.setText(f"VIDAS RESTANTES: {vidas}")
        self.label_puntaje_total.setText(f"PUNTAJE OBTENIDO: {puntaje}")
        self.label_nombre.setText(f"NOMBRE: {nombre}")

        self.show()

    def ocultar(self):
        self.hide()
        # self.senal_detener_musica.emit()
        sys.exit()

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaDerrota()
    ventana.mostrar()
    sys.exit(app.exec())