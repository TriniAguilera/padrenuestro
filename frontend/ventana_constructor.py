import typing
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, Qt, QRect, QPoint, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QMessageBox, QLineEdit, QPushButton, QComboBox, \
    QHBoxLayout, QVBoxLayout, QGridLayout, QApplication)
import parametros as p

class VentanaConstructor(QWidget):

    senal_dificultad = pyqtSignal(str)
    senal_boton_actual_izquierdo = pyqtSignal(str)
    senal_casilla_presionada = pyqtSignal(int, int)
    senal_agregar_letra_tablero = pyqtSignal(str, int, int)
    senal_revisar_luigi_y_estrella = pyqtSignal(int, int)
    senal_crear_txt = pyqtSignal()
    senal_pedir_botones_presionados = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.cantidad_luigi = p.MAXIMO_LUIGI #################### CAMBIARLO A PARAMETROS
        self.cantidad_estrella = p.MAXIMO_ESTRELLA #################### CAMBIARLO A PARAMETROS
        self.cantidad_pared = p.MAXIMO_PARED #################### CAMBIARLO A PARAMETROS
        self.cantidad_roca = p.MAXIMO_ROCA #################### CAMBIARLO A PARAMETROS
        self.cantidad_fuego = p.MAXIMO_FUEGO #################### CAMBIARLO A PARAMETROS
        self.cantidad_fantasma_horizontal_blanco = p.MAXIMO_FANTASMAS_HORIZONTAL 
        self.cantidad_fantasma_vertical_rojo = p.MAXIMO_FANTASMAS_VERTICAL 
        self.label_casillas_grilla = {}
        self.init_gui()

    def init_gui(self):
        self.setGeometry(100, 100, 1000, 900)
        self.setWindowTitle("Ventana Constructor")

        self.widget_principal_horizontal = QWidget(self)
        self.layout_principal_horizontal = QHBoxLayout()

        self.comboBox_juego = QComboBox(self)
        self.comboBox_juego.setObjectName("comboBox_juego")
        self.comboBox_juego.setGeometry(QRect(QPoint(20, 10), QSize(320, 42)))
        self.comboBox_juego.addItem("Todos")
        self.comboBox_juego.addItem("Bloques")
        self.comboBox_juego.addItem("Entidades")
        self.comboBox_juego.setFont(QFont("calibri", 12))
        self.comboBox_juego.activated.connect(self.cambiar_dificultad)

        ### Luigi
        self.boton_luigi = QPushButton(self)
        self.boton_luigi.setObjectName("boton_luigi")
        self.boton_luigi.setGeometry(QRect(QPoint(20, 60), QSize(270, 42)))
        self.boton_luigi.setText(f"({self.cantidad_luigi})")
        self.boton_luigi.setFont(QFont("calibri", 12))
        self.boton_luigi.clicked.connect(self.boton_actual_izquierdo)
        self.label_luigi = QLabel(self)
        self.label_luigi.setGeometry(QRect(QPoint(300, 60), QSize(42, 42)))

        ### estrella
        self.boton_estrella = QPushButton(self)
        self.boton_estrella.setObjectName("boton_estrella")
        self.boton_estrella.setGeometry(QRect(QPoint(20, 110), QSize(270, 42)))
        self.boton_estrella.setText(f"({self.cantidad_estrella})")
        self.boton_estrella.setFont(QFont("calibri", 12))
        self.boton_estrella.clicked.connect(self.boton_actual_izquierdo)
        self.label_estrella = QLabel(self)
        self.label_estrella.setGeometry(QRect(QPoint(300, 110), QSize(42, 42)))

        ### fantasma horizontal/blanco
        self.boton_fantasma_horizontal = QPushButton(self)
        self.boton_fantasma_horizontal.setObjectName("boton_fantasma_horizontal")
        self.boton_fantasma_horizontal.setGeometry(QRect(QPoint(20, 160), QSize(270, 42)))
        self.boton_fantasma_horizontal.setText(f"({self.cantidad_fantasma_horizontal_blanco})")
        self.boton_fantasma_horizontal.setFont(QFont("calibri", 12))
        self.boton_fantasma_horizontal.clicked.connect(self.boton_actual_izquierdo)
        self.label_fantasma_horizontal = QLabel(self)
        self.label_fantasma_horizontal.setGeometry(QRect(QPoint(300, 160), QSize(42, 42)))

        ### fantasma vertical/rojo
        self.boton_fantasma_vertical = QPushButton(self)
        self.boton_fantasma_vertical.setObjectName("boton_fantasma_vertical")
        self.boton_fantasma_vertical.setGeometry(QRect(QPoint(20, 210), QSize(270, 42)))
        self.boton_fantasma_vertical.setText(f"({self.cantidad_fantasma_vertical_rojo})")
        self.boton_fantasma_vertical.setFont(QFont("calibri", 12))
        self.boton_fantasma_vertical.clicked.connect(self.boton_actual_izquierdo)
        self.label_fantasma_vertical = QLabel(self)
        self.label_fantasma_vertical.setGeometry(QRect(QPoint(300, 210), QSize(42, 42)))

        ### pared
        self.boton_pared = QPushButton(self)
        self.boton_pared.setObjectName("boton_pared")
        self.boton_pared.setGeometry(QRect(QPoint(20, 260), QSize(270, 42)))
        self.boton_pared.setText(f"({self.cantidad_pared})")
        self.boton_pared.setFont(QFont("calibri", 12))
        self.boton_pared.clicked.connect(self.boton_actual_izquierdo)
        self.label_pared = QLabel(self)
        self.label_pared.setGeometry(QRect(QPoint(300, 260), QSize(42, 42)))

        ### roca
        self.boton_roca = QPushButton(self)
        self.boton_roca.setObjectName("boton_roca")
        self.boton_roca.setGeometry(QRect(QPoint(20, 310), QSize(270, 42)))
        self.boton_roca.setText(f"({self.cantidad_roca})")
        self.boton_roca.setFont(QFont("calibri", 12))
        self.boton_roca.clicked.connect(self.boton_actual_izquierdo)
        self.label_roca = QLabel(self)
        self.label_roca.setGeometry(QRect(QPoint(300, 310), QSize(42, 42)))

        ### fuego
        self.boton_fuego = QPushButton(self)
        self.boton_fuego.setObjectName("boton_fuego")
        self.boton_fuego.setGeometry(QRect(QPoint(20, 360), QSize(270, 42)))
        self.boton_fuego.setText(f"({self.cantidad_fuego})")
        self.boton_fuego.setFont(QFont("calibri", 12))
        self.boton_fuego.clicked.connect(self.boton_actual_izquierdo)
        self.label_fuego = QLabel(self)
        self.label_fuego.setGeometry(QRect(QPoint(300, 360), QSize(42, 42)))

        ### limpiar
        self.boton_limpiar_constructor = QPushButton(self)
        self.boton_limpiar_constructor.setObjectName("boton_limpiar_constructor")
        self.boton_limpiar_constructor.setGeometry(QRect(QPoint(25, 800), QSize(150, 42)))
        self.boton_limpiar_constructor.setText("Limpiar tablero")
        self.boton_limpiar_constructor.setFont(QFont("calibri", 12))
        self.boton_limpiar_constructor.clicked.connect(self.limpiar_tablero)

        ### jugar
        self.boton_jugar_constructor = QPushButton(self)
        self.boton_jugar_constructor.setObjectName("boton_jugar_constructor")
        self.boton_jugar_constructor.setGeometry(QRect(QPoint(185, 800), QSize(150, 42)))
        self.boton_jugar_constructor.setText("Jugar")
        self.boton_jugar_constructor.setFont(QFont("calibri", 12))
        self.boton_jugar_constructor.clicked.connect(self.jugar)

        ### salir
        self.boton_salir_constructor = QPushButton(self)
        self.boton_salir_constructor.setObjectName("boton_salir_constructor")
        self.boton_salir_constructor.setGeometry(QRect(QPoint(100, 750), QSize(150, 42)))
        self.boton_salir_constructor.setText("Salir")
        self.boton_salir_constructor.setFont(QFont("calibri", 12))
        self.boton_salir_constructor.clicked.connect(self.salir)

        self.widget_izquierdo = QWidget(self)
        self.layout_izquierdo = QVBoxLayout()
        self.layout_principal_horizontal.addLayout(self.layout_izquierdo)

        self.crear_label_entidad(); self.crear_label_bloque()
        self.crear_grilla()

    def crear_grilla(self):
        ### hacemos grilla del tablero
        self.widget_grilla = QWidget(self)
        self.widget_grilla.setGeometry(QRect(QPoint(360, 10), QSize(620, 870)))
        self.layout_grilla = QGridLayout()
        self.layout_grilla.setHorizontalSpacing(1)
        self.layout_grilla.setVerticalSpacing(1)
        self.widget_grilla.setLayout(self.layout_grilla)
        self.widget_grilla.setStyleSheet("""
            background-color: #c48027;
            border-color: 1px solid #000000;
        """)

        ### agregamos los cuadrados a la grilla
        for fila in range(16):
            for columna in range(11):
                # casilla = QLabel(self)
                # casilla.setFixedSize(52, 52)
                # casilla.setStyleSheet("background-color: #d1a77a")
                # casilla.setObjectName(f"{fila}_{columna}")
                # self.label_casillas_grilla[f"{fila}_{columna}"] = casilla
                # self.layout_grilla.addWidget(casilla, fila, columna)
                # boton_casilla = QPushButton(self)
                # boton_casilla.setObjectName(f"{fila}_{columna}")
                # boton_casilla.setStyleSheet(
                #     "background-color: rgba(0, 0, 0, 0); border: none;")
                # boton_casilla.clicked.connect(self.casilla_presionada)
                # boton_casilla.setFixedSize(52, 52)
                # self.layout_grilla.addWidget(boton_casilla, fila, columna)
                if fila == 0 or fila == 15 or columna == 0 or columna == 10:
                    casilla = QLabel(self)
                    casilla.setStyleSheet("background-color: #d1a77a")
                    ruta_foto = p.RUTA_DESIERTO_CORTADO ########### cambiarlo a PARAMETROS 
                    foto = QPixmap(ruta_foto)
                    casilla.setPixmap(foto)
                    casilla.setScaledContents(True)
                    casilla.setFixedSize(52, 52)
                    casilla.setObjectName(f"{fila}_{columna}")
                    self.label_casillas_grilla[f"{fila}_{columna}"] = casilla
                    self.layout_grilla.addWidget(casilla, fila, columna)
                else:
                    casilla = QLabel(self)
                    casilla.setFixedSize(52, 52)
                    casilla.setStyleSheet("background-color: #d1a77a")
                    casilla.setObjectName(f"{fila}_{columna}")
                    self.label_casillas_grilla[f"{fila}_{columna}"] = casilla
                    self.layout_grilla.addWidget(casilla, fila, columna)
                    boton_casilla = QPushButton(self)
                    boton_casilla.setObjectName(f"{fila}_{columna}")
                    boton_casilla.setStyleSheet(
                        "background-color: rgba(0, 0, 0, 0); border: none;")
                    boton_casilla.clicked.connect(self.casilla_presionada)
                    boton_casilla.setFixedSize(52, 52)
                    self.layout_grilla.addWidget(boton_casilla, fila, columna)
        self.layout_principal_horizontal.addWidget(self.widget_grilla)

    def crear_label_entidad(self):
        self.label_luigi.setPixmap(QPixmap(p.RUTA_LUIGI_FRONT)) ########### cambiarlo a PARAMETROS
        self.label_luigi.setScaledContents(True)
        self.label_fantasma_horizontal.setPixmap(QPixmap(p.RUTA_WHITE_GHOST_RIGHT_1)) 
        self.label_fantasma_horizontal.setScaledContents(True)
        self.label_fantasma_vertical.setPixmap(QPixmap(p.RUTA_RED_GHOST_VERTICAL_1)) 
        self.label_fantasma_vertical.setScaledContents(True)

    def crear_label_bloque(self):
        self.label_estrella.setPixmap(QPixmap(p.RUTA_ESTRELLA)) ########### cambiarlo a PARAMETROS
        self.label_estrella.setScaledContents(True)
        self.label_pared.setPixmap(QPixmap(p.RUTA_PARED)) ########### cambiarlo a PARAMETROS
        self.label_pared.setScaledContents(True)
        self.label_roca.setPixmap(QPixmap(p.RUTA_ROCA)) ########### cambiarlo a PARAMETROS
        self.label_roca.setScaledContents(True)
        self.label_fuego.setPixmap(QPixmap(p.RUTA_FUEGO)) ########### cambiarlo a PARAMETROS
        self.label_fuego.setScaledContents(True)

    def casilla_presionada(self):
        sender = self.sender()
        nombre_boton = sender.objectName()
        lista_nombre_boton = nombre_boton.split("_")
        fila = lista_nombre_boton[0]
        columna = lista_nombre_boton[1]
        self.senal_casilla_presionada.emit(int(fila), int(columna))

    def pop_up_error_constructor(self, lista):
        if type(lista[0]) == tuple:
            tupla = lista[0]
            fila = tupla[0]
            columna = tupla[1]
            QMessageBox.about(self, "ERROR", f"No se puede agregar elemento a casilla "\
                              f"({fila}, {columna}). \nSeleccione otra.")
        elif lista[0] == "no juego":
            QMessageBox.about(self, "ERROR", "Falta agregar al tablero a Luigi o la Estrella "\
                            "o ambos.")
        else:
            QMessageBox.about(self, "ERROR", f"Debe seleccionar primero un elemento para "\
                              f"insertarlo en el tablero")
            
    def agregar_elemento_tablero(self, boton_izq, fila_str, columna_str):
        fila = int(fila_str)
        columna = int(columna_str)
        print("Vamos a agregar imagen elemento en ventana constructor")
        if boton_izq == "L" and self.cantidad_luigi > 0:
            ruta = p.RUTA_LUIGI_FRONT ########### cambiarlo a PARAMETROS
            self.cantidad_luigi -= 1
        elif boton_izq == "S" and self.cantidad_estrella > 0:
            ruta = p.RUTA_ESTRELLA ########### cambiarlo a PARAMETROS
            self.cantidad_estrella -= 1
        elif boton_izq == "V" and self.cantidad_fantasma_vertical_rojo > 0:
            ruta = p.RUTA_RED_GHOST_VERTICAL_1 ########### cambiarlo a PARAMETROS
            self.cantidad_fantasma_vertical_rojo -= 1
        elif boton_izq == "H" and self.cantidad_fantasma_horizontal_blanco > 0:
            ruta = p.RUTA_WHITE_GHOST_RIGHT_1 ########### cambiarlo a PARAMETROS
            self.cantidad_fantasma_horizontal_blanco -= 1
        elif boton_izq == "P" and self.cantidad_pared > 0:
            ruta = p.RUTA_PARED ########### cambiarlo a PARAMETROS
            self.cantidad_pared -= 1
        elif boton_izq == "R" and self.cantidad_roca > 0:
            ruta = p.RUTA_ROCA ########### cambiarlo a PARAMETROS
            self.cantidad_roca -= 1
        elif boton_izq == "F" and self.cantidad_fuego > 0:
            ruta = p.RUTA_FUEGO ########### cambiarlo a PARAMETROS
            self.cantidad_fuego -= 1

        llave_casilla = f"{str(fila)}_{str(columna)}"
        self.label_casillas_grilla[llave_casilla].setStyleSheet("background-color: #d1a77a")
        self.label_casillas_grilla[llave_casilla].setPixmap(QPixmap(ruta))
        self.label_casillas_grilla[llave_casilla].setScaledContents(True)
        print("Ya agregamos elemento al tablero")
        self.actualizar_botones_izquierdos()
        self.senal_agregar_letra_tablero.emit(boton_izq, fila, columna)
        self.senal_boton_actual_izquierdo.emit("None") 

    def actualizar_botones_izquierdos(self):
        self.boton_luigi.setText(f"({self.cantidad_luigi})")
        self.boton_luigi.setFont(QFont("calibri", 12))
        self.boton_estrella.setText(f"({self.cantidad_estrella})")
        self.boton_estrella.setFont(QFont("calibri", 12))
        self.boton_fantasma_horizontal.setText(f"({self.cantidad_fantasma_horizontal_blanco})")
        self.boton_fantasma_horizontal.setFont(QFont("calibri", 12))
        self.boton_fantasma_vertical.setText(f"({self.cantidad_fantasma_vertical_rojo})")
        self.boton_fantasma_vertical.setFont(QFont("calibri", 12))
        self.boton_pared.setText(f"({self.cantidad_pared})")
        self.boton_pared.setFont(QFont("calibri", 12))
        self.boton_roca.setText(f"({self.cantidad_roca})")
        self.boton_roca.setFont(QFont("calibri", 12))
        self.boton_fuego.setText(f"({self.cantidad_fuego})")
        self.boton_fuego.setFont(QFont("calibri", 12))

    def boton_actual_izquierdo(self):
        sender = self.sender()
        nombre_boton = sender.objectName()
        print(f"Sender: {nombre_boton}")
        if nombre_boton == "boton_luigi" and self.cantidad_luigi > 0:
            self.senal_boton_actual_izquierdo.emit("L")
        elif nombre_boton == "boton_estrella" and self.cantidad_estrella > 0:
            self.senal_boton_actual_izquierdo.emit("S")
        elif nombre_boton == "boton_fantasma_horizontal" and \
            self.cantidad_fantasma_horizontal_blanco > 0:
            self.senal_boton_actual_izquierdo.emit("H")
        elif nombre_boton == "boton_fantasma_vertical" and self.cantidad_fantasma_vertical_rojo > 0:
            self.senal_boton_actual_izquierdo.emit("V")
        elif nombre_boton == "boton_pared" and self.cantidad_pared > 0:
            self.senal_boton_actual_izquierdo.emit("P")
        elif nombre_boton == "boton_roca" and self.cantidad_roca > 0:
            self.senal_boton_actual_izquierdo.emit("R")
        elif nombre_boton == "boton_fuego" and self.cantidad_fuego > 0:
            self.senal_boton_actual_izquierdo.emit("F")

    def activar_bloque(self):
        self.boton_pared.setEnabled(True)
        self.boton_roca.setEnabled(True)
        self.boton_fuego.setEnabled(True)
        self.boton_estrella.setEnabled(True)
        self.boton_pared.setStyleSheet("color: black; border-color: black")
        self.boton_roca.setStyleSheet("color: black; border-color: black")
        self.boton_fuego.setStyleSheet("color: black; border-color: black")
        self.boton_estrella.setStyleSheet("color: black; border-color: black")
        self.crear_label_bloque()

    def activar_entidad(self):
        self.boton_luigi.setEnabled(True)
        self.boton_fantasma_vertical.setEnabled(True)
        self.boton_fantasma_horizontal.setEnabled(True)
        self.boton_luigi.setStyleSheet("color: black; border-color: black")
        self.boton_fantasma_vertical.setStyleSheet("color: black; border-color: black")
        self.boton_fantasma_horizontal.setStyleSheet("color: black; border-color: black")
        self.crear_label_entidad()

    def descativar_bloque(self):
        self.boton_pared.setEnabled(False)
        self.boton_roca.setEnabled(False)
        self.boton_fuego.setEnabled(False)
        self.boton_estrella.setEnabled(False)
        self.boton_pared.setStyleSheet("background: transparent; color: transparent")
        self.label_pared.clear()
        self.boton_roca.setStyleSheet("background: transparent; color: transparent")
        self.label_roca.clear()
        self.boton_fuego.setStyleSheet("background: transparent; color: transparent")
        self.label_fuego.clear()
        self.boton_estrella.setStyleSheet("background: transparent; color: transparent")
        self.label_estrella.clear()
    
    def desactivar_entidad(self):
        self.boton_luigi.setEnabled(False)
        self.boton_fantasma_vertical.setEnabled(False)
        self.boton_fantasma_horizontal.setEnabled(False)
        self.boton_luigi.setStyleSheet("background: transparent; color: transparent")
        self.label_luigi.clear()
        self.boton_fantasma_vertical.setStyleSheet("background: transparent; color: transparent")
        self.label_fantasma_vertical.clear()
        self.boton_fantasma_horizontal.setStyleSheet("background: transparent; color: transparent")
        self.label_fantasma_horizontal.clear()

    def todos(self):
        self.activar_bloque(); self.crear_label_bloque()
        self.activar_entidad(); self.crear_label_entidad()

    def bloque(self):
        self.activar_bloque(); self.desactivar_entidad()

    def entidad(self):
        self.activar_entidad(); self.descativar_bloque()

    def cambiar_dificultad(self):
        actual = str(self.comboBox_juego.currentText())
        print(f"La dificultado actual es: {actual}")
        self.senal_dificultad.emit(actual)

    def limpiar_tablero(self):
        print("Voy a limpiar el tablero")
        self.cantidad_luigi = p.MAXIMO_LUIGI #################### CAMBIARLO A PARAMETROS
        self.cantidad_estrella = p.MAXIMO_ESTRELLA #################### CAMBIARLO A PARAMETROS
        self.cantidad_pared = p.MAXIMO_PARED #################### CAMBIARLO A PARAMETROS
        self.cantidad_roca = p.MAXIMO_ROCA #################### CAMBIARLO A PARAMETROS
        self.cantidad_fuego = p.MAXIMO_FUEGO #################### CAMBIARLO A PARAMETROS
        self.cantidad_fantasma_horizontal_blanco = p.MAXIMO_FANTASMAS_HORIZONTAL 
        self.cantidad_fantasma_vertical_rojo = p.MAXIMO_FANTASMAS_VERTICAL 
        self.actualizar_botones_izquierdos()
        self.senal_pedir_botones_presionados.emit()

    def limpiar_lables_grilla(self, lista_botones):
        for tupla in lista_botones:
            fila = tupla[0]; columna = tupla[1]
            llave_casilla = f"{str(fila)}_{str(columna)}"
            self.label_casillas_grilla[llave_casilla].clear()
            self.label_casillas_grilla[llave_casilla].setStyleSheet("background-color: #d1a77a")

    def jugar(self):
        print("Vamos a intentar jugar")
        luigi = self.cantidad_luigi; estrella = self.cantidad_estrella
        self.senal_revisar_luigi_y_estrella.emit(luigi, estrella)

    def respuesta_revision(self, boleeano):
        if boleeano == True:
            self.ocultar(); self.senal_crear_txt.emit()
        else:
            self.pop_up_error_constructor(["no juego"])

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()

    def salir(self):
        self.hide()
        sys.exit()